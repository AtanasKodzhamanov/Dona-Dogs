import datetime
import json
from django import template
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from DogShelter.web.forms import SubscribeForm, DogFilterForm, vaStatusForm, genderFilterForm, ContactForm
from DogShelter.web.models import Dog, DonationStory, NoticeBoard, LongPost, Donation
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _


# responsible for the subscribe form in the footnote of every page

# ----- Utility functions -----


def handler404(request, exception):
    return render(request, '404.html', status=404)


def renderCommon(request):
    subscribeForm = SubscribeForm(request.POST or None)
    return subscribeForm


def handle_form_post(request, template_name=None, context=None):
    form = SubscribeForm(request.POST)
    if form.is_valid():
        form.save()

    context = context or {}
    context.update({'subscribe_form': form})
    return render(request, template_name, context=context)

# ----- Views -----

# BaseDataView is the base class for all views that need to access the common context data (e.g. notice board, content container, subscribe form, etc.)


class BaseView(TemplateView):
    def get_template_name(self):
        # This should be implemented by subclasses
        raise NotImplementedError

    def get_common_context_data(self):
        context = {}

        # get all notice board items from the database
        context['data_notice_board'] = NoticeBoard.objects.all().order_by("order")

        # get all content container items from the database
        context['content_container'] = LongPost.objects.all().order_by("order")

        context['content_containter_pics'] = [
            f'about_pic_{i}' for i in range(1, 11)]

        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_common_context_data())
        return context


class HomeView(BaseView):
    template_name = "home.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # get all dogs from the database
        data_dogs = Dog.objects.filter(
            status__in=["Active", "Sick", "New"]).order_by("?")
        data_dogs = data_dogs[:6]

        today = datetime.date.today()
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        date_pk = last_month.strftime("%Y-%b")

        donation_stories = DonationStory.objects.filter(date=last_month)

        # statistics for the home page
        count_dogs = Dog.objects.filter(
            status__in=["Active", "Sick", "New"]).count()
        count_sick = Dog.objects.filter(status="Sick").count()
        cound_adopted_last_year = Dog.objects.filter(
            adoption_year=today.year-1).count()

        # filter away adopted dogs where there is no post adoption pic available and return a random dog
        adopted = Dog.objects.filter(adoption_year=today.year-1)
        adopted = adopted.exclude(adoption_pic_after_1="")
        adopted = adopted.order_by("?").first()

        context.update({
            # statistics for the home page
            "adopted_puppy": adopted,
            "count_dogs": count_dogs,
            "count_sick": count_sick,
            "count_adopted_last_year": cound_adopted_last_year,

            # donations slideshow data
            "donation_stories": donation_stories,

            # core dog data
            "data_dogs": data_dogs,

            # date for the donations slideshow
            "date_pk": date_pk,

            # subscribe form
            "subscribe_form": SubscribeForm(self.request.POST or None),
        })

        return context

    def post(self, request):
        return handle_form_post(
            request,
            template_name='home.html',
            context=self.get_common_context_data()
        )


# responsible for showing the monthly donation summary pages
class DonationStoryView(TemplateView):
    model = DonationStory
    template_name = "donationMonthly.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_pk'] = self.kwargs['date_pk']

        date = datetime.datetime.strptime(self.kwargs['date_pk'], '%Y-%b')

        # filter Donation model data to get the names of the donors for this month
        donation_names = Donation.objects.filter(
            date__year=date.year, date__month=date.month)

        # filter DonationStory for this month to get the non-monetary donations for this month (e.g. food, blankets, etc.)
        donations = self.model.objects.filter(
            date__year=date.year, date__month=date.month)

        # create a list of the donation_pic_1, donation_pic_2, etc. image fields for the template to loop through
        # convert the Donation model data to a dictionary so that it can be passed to the template and looped through
        donation_pic_fields = [f'donation_pic_{i}' for i in range(1, 7)]

        # return context
        context['donation_pic_fields'] = donation_pic_fields
        context['donation_names'] = donation_names
        context['donations'] = donations
        context["date"] = date

        # common context data
        context['subscribe_form'] = SubscribeForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        return handle_form_post(request, template_name=self.template_name, context={
            'date_pk': self.kwargs['date_pk'],
            **self.get_context_data()
        })


# responsible for showing the individual dog profile pages


class DogProfileView(DetailView):
    model = Dog
    template_name = "dogProfile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all dogs with a status of "active"
        active_dogs = Dog.objects.filter(status__in=["Active", "Sick", "New"])

        # Extract the IDs of the active dogs into an array
        active_dog_ids = [dog.id for dog in active_dogs]
        active_dog_ids.reverse()

        # create a list of the pic_2, pic_3, etc. image fields for the template to loop through
        dog_pic_fields = [f'pic_{i}' for i in range(2, 7)]
        adoption_pic_fields = [f'adoption_pic_after_{i}' for i in range(1, 4)]

        # return context
        context['adoption_pic_fields'] = adoption_pic_fields
        context['dog_pic_fields'] = dog_pic_fields
        context['active_dog_ids'] = json.dumps(active_dog_ids)

        # common context data
        context['subscribe_form'] = SubscribeForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return handle_form_post(request, template_name=self.template_name, context={
            'pk': self.kwargs['pk'],
            'object': self.object,  # Add the object to the context dictionary
            **self.get_context_data(**kwargs)
        })


# responsible for rendering the gallery page


class GalleryView(BaseView):
    template_name = "dogGallery.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add forms to the context
        context['gender_filter_form'] = genderFilterForm()
        context['name_filter_form'] = DogFilterForm()
        context['va_status_form'] = vaStatusForm()

        # add dog and virtual adopter data to the context
        context['new_dogs'] = Dog.objects.filter(
            status__in=["New"])
        context['active_dogs'] = Dog.objects.filter(
            status__in=["Active", "Sick"]).order_by("-arrival_year")
        context['data_people'] = set(Dog.objects.values_list(
            "va_name_bg", "va_name_eng").exclude(va_name_eng=""))
        context['subscribe_form'] = SubscribeForm(self.request.POST or None)

        return context

    def post(self, request):
        return handle_form_post(
            request,
            template_name='dogGallery.html',
            context=self.get_common_context_data()
        )


# responsible for rendering the clinic page


class ClinicView(BaseView):
    template_name = "clinic.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add infirmary-specific data to the context
        data_dogs = Dog.objects.filter(status="Sick").order_by("?")

        context.update({
            "data_dogs": data_dogs,
            "subscribe_form": SubscribeForm(self.request.POST or None),
        })

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)

    def post(self, request):
        return handle_form_post(
            request,
            template_name='clinic.html',
            context=self.get_common_context_data()
        )


# renders the about page

class AboutView(BaseView):
    template_name = "ourstory.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()
        context.update({
            "subscribe_form": SubscribeForm(self.request.POST or None),
        })

        return context

    def post(self, request):
        return handle_form_post(
            request,
            template_name='ourstory.html',
            context=self.get_common_context_data()
        )


# renders the adoption page


class AdoptionsView(BaseView):
    template_name = "adoptions.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add adoptions-specific data to the context
        data_dogs = serializers.serialize(
            'python', Dog.objects.all().order_by("-adoption_year"))
        dogs = Dog.objects.all().filter(adoption_year__gt=0).order_by("-adoption_year")
        years = sorted(set(dogs.values_list(
            "adoption_year", flat=True)), reverse=True)
        field_names = ['pic_2', 'pic_3', 'pic_4', 'pic_5', 'pic_6', 'adoption_pic_after_1',
                       'adoption_pic_after_2', 'adoption_pic_after_3']
        context.update({
            "data_dogs": data_dogs,
            "dogs": dogs,
            "years": years,
            "field_names": field_names,
            "subscribe_form": SubscribeForm(self.request.POST or None)
        })
        return context

    def post(self, request):
        return handle_form_post(
            request,
            template_name='adoptions.html',
            context=self.get_common_context_data()
        )


# renders the donations page


class DonationsView(BaseView):
    template_name = "donations.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add donations-specific data to the context
        data_people = set(Dog.objects.values_list(
            "va_name_bg", "va_name_eng").exclude(va_name_eng=""))
        today = datetime.date.today()
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        last_month_cl = "("+last_month.strftime('%m') + \
            " - " + last_month.strftime('%Y') + ")"
        data_donations = set(Donation.objects.values_list(
            "person_name_bg", "person_name_eng").filter(date=last_month).order_by("person_name_bg"))

        context.update({
            "data_people": data_people,
            "last_month": last_month,
            "month": last_month_cl,
            "data_donations": data_donations,
            "subscribe_form": SubscribeForm(self.request.POST or None)
        })

        return context

    def post(self, request):
        return handle_form_post(
            request,
            template_name='donations.html',
            context=self.get_common_context_data()
        )


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, _("Thank you for your message!"))
            return redirect('contact')
        else:
            messages.error(
                request, _("Error, please try again or message us on our email..."))
    else:
        form = ContactForm()

    # Render the contact form (you need to create this template)
    return render(request, 'contact.html', {'form': form})
