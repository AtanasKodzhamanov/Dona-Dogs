import datetime
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.generic import DetailView, ListView, TemplateView
from DogShelter.web.forms import SubscribeForm, DogFilterForm, vaStatusForm, genderFilterForm
from DogShelter.web.models import Dog, DonationStory, NoticeBoard, LongPost, Donation

# responsible for the subscribe form in the footnote of every page

# ----- Utility functions -----


def renderCommon(request):
    if request.method == "GET":
        subscribeForm = SubscribeForm()
    else:
        subscribeForm = SubscribeForm(request.POST or None)
        if subscribeForm.is_valid():
            subscribeForm.save()
    return subscribeForm

# ----- Views -----

# BaseDataView is the base class for all views that need to access the common context data (e.g. notice board, content container, subscribe form, etc.)


class BaseView(TemplateView):
    def get_template_name(self):
        # This should be implemented by subclasses
        raise NotImplementedError

    def get_common_context_data(self):
        context = {}

        # get all notice board items from the database
        context['dataNoticeBoard'] = serializers.serialize(
            'python', NoticeBoard.objects.all().order_by("order"))

        # get all content container items from the database
        context['contentContainer'] = serializers.serialize(
            'python', LongPost.objects.all().order_by("order"))

        context['content_containter_pics'] = [
            f'about_pic_{i}' for i in range(1, 11)]

        # get the subscribe form for the footer
        context['subscribeForm'] = renderCommon(self.request)

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
        dataDogs = serializers.serialize(
            'python', Dog.objects.all().order_by("?"))

        # filter for the active dogs only (alive, healthy and not adopted) and pick 6 random dogs to display on the home page
        dataDogs = [dog for dog in dataDogs if dog['fields']
                    ['status'] == 'Active']
        dataDogs = dataDogs[:6]

        today = datetime.date.today()
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        date_pk = last_month.strftime("%Y-%b")

        donation_stories = DonationStory.objects.filter(date=last_month)

        # statistics for the home page
        countDogs = Dog.objects.filter(status__in=["Active", "Sick"]).count()
        countSick = Dog.objects.filter(status="Sick").count()
        countAdoptedLastYear = Dog.objects.filter(
            adoption_year=today.year-1).count()

        # filter away adopted dogs where there is no post adoption pic available and return a random dog
        adopted = Dog.objects.filter(adoption_year=today.year-1)
        adopted = adopted.exclude(adoption_pic_after_1="")
        adopted = adopted.order_by("?").first()

        context.update({
            # statistics for the home page
            "adoptedPuppy": adopted,
            "countDogs": countDogs,
            "countSick": countSick,
            "countAdoptedLastYear": countAdoptedLastYear,

            # donations slideshow data
            "donation_stories": donation_stories,

            # core dog data
            "dataDogs": dataDogs,

            # date for the donations slideshow
            "date_pk": date_pk,
        })

        return context

# responsible for showing the monthly donation summary pages


class DonationStoryView(ListView):
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
        donations_data = [model_to_dict(donation) for donation in donations]

        # return context
        context['donation_pic_fields'] = donation_pic_fields
        context['donation_names'] = donation_names
        context['donations'] = donations_data

        # common context data
        context['subscribeForm'] = renderCommon(self.request)
        return context

# responsible for showing the individual dog profile pages


class DogProfileView(DetailView):
    model = Dog
    template_name = "dogProfile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # create a list of the pic_2, pic_3, etc. image fields for the template to loop through
        dog_pic_fields = [f'pic_{i}' for i in range(2, 7)]
        adoption_pic_fields = [f'adoption_pic_after_{i}' for i in range(1, 4)]

        # return context
        context['adoption_pic_fields'] = adoption_pic_fields
        context['dog_pic_fields'] = dog_pic_fields

        # common context data
        context['subscribeForm'] = renderCommon(self.request)
        return context

# responsible for rendering the gallery page


class GalleryView(BaseView):
    template_name = "dogGallery.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add forms to the context
        context['genderFilterForm'] = genderFilterForm()
        context['nameFilterForm'] = DogFilterForm()
        context['vaStatusForm'] = vaStatusForm()

        # add dog and virtual adopter data to the context
        context['dataDogs'] = serializers.serialize(
            'python', Dog.objects.all().order_by("?"))
        context['dataPeople'] = set(Dog.objects.values_list(
            "va_name_bg", "va_name_eng").exclude(va_name_eng=""))

        return context


# responsible for rendering the clinic page


class ClinicView(BaseView):
    template_name = "clinic.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add infirmary-specific data to the context
        dataDogs = serializers.serialize(
            'python', Dog.objects.filter(status="Sick").order_by("?"))

        context.update({
            "dataDogs": dataDogs
        })

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


# renders the about page

class AboutView(BaseView):
    template_name = "ourstory.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        return context


# renders the adoption page


class AdoptionsView(BaseView):
    template_name = "adoptions.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add adoptions-specific data to the context
        dataDogs = serializers.serialize(
            'python', Dog.objects.all().order_by("-adoption_year"))
        dogs = Dog.objects.all().filter(adoption_year__gt=0).order_by("-adoption_year")
        years = sorted(set(dogs.values_list(
            "adoption_year", flat=True)), reverse=True)
        field_names = ['pic_2', 'pic_3', 'pic_4', 'pic_5', 'pic_6', 'adoption_pic_after_1',
                       'adoption_pic_after_2', 'adoption_pic_after_3']
        context.update({
            "dataDogs": dataDogs,
            "dogs": dogs,
            "years": years,
            "field_names": field_names
        })
        return context


# renders the donations page


class DonationsView(BaseView):
    template_name = "donations.html"

    def get_common_context_data(self):
        context = super().get_common_context_data()

        # add donations-specific data to the context
        dataPeople = set(Dog.objects.values_list(
            "va_name_bg", "va_name_eng").exclude(va_name_eng=""))
        today = datetime.date.today()
        last_month = today.replace(day=1) - datetime.timedelta(days=1)
        last_month_cl = "("+last_month.strftime('%m') + \
            " - " + last_month.strftime('%Y') + ")"
        dataDonations = set(Donation.objects.values_list(
            "person_name_bg", "person_name_eng").filter(date=last_month).order_by("person_name_bg"))

        context.update({
            "dataPeople": dataPeople,
            "last_month": last_month,
            "month": last_month_cl,
            "dataDonations": dataDonations
        })

        return context
