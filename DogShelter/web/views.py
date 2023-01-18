import datetime
from django import views
from django.core import serializers
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
import django.utils.translation
from DogShelter.web.forms import SubscribeForm, ContactForm, AdoptForm, DogFilterForm, vaStatusForm, genderFilterForm
from DogShelter.web.models import Dog, DonationStory, NoticeBoard, About, Donation
from django.utils.translation import activate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView, ListView

# Create your views here.
# class SignUpView(views.CreateView):
#     form_class = UserCreationForm
#     template_name = 'auth/signup.html'
#     success_url = reverse_lazy('sign_up')

# class SignUpForm(auth.forms.UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


def renderCommon(request):
    if request.method == "get":
        subscribeForm = SubscribeForm()
    else:
        subscribeForm = SubscribeForm(request.POST or None)
        if subscribeForm.is_valid():
            subscribeForm.save()
    return subscribeForm


class show_donation_story(ListView):
    model = DonationStory
    template_name = "donationMonthly.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_pk'] = self.kwargs['date_pk']

        date = datetime.datetime.strptime(self.kwargs['date_pk'], '%Y-%b')

        # filter Donation for this month
        donation_names = Donation.objects.filter(
            date__year=date.year, date__month=date.month)

        # filter DonationStory for this month
        donations = self.model.objects.filter(
            date__year=date.year, date__month=date.month)

        # return context into donationNames and donationStories
        context['donation_names'] = donation_names
        context['donations'] = donations
        context['subscribeForm'] = renderCommon(self.request)
        return context


class show_dog(DetailView):
    model = Dog
    template_name = "dogProfile.html"
    queryset = Dog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscribeForm'] = renderCommon(self.request)
        return context


def show_all_dogs(request):
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataPeople = set(Dog.objects.values_list(
        "va_name_bg", "va_name_eng").exclude(va_name_eng=""))
    genderForm = genderFilterForm()
    nameForm = DogFilterForm()
    vaForm = vaStatusForm()
    contactForm = ContactForm()
    adoptForm = AdoptForm()

    context = {
        'subscribeForm': renderCommon(request),
        "genderFilterForm": genderForm,
        "adoptForm": adoptForm,
        "contactForm": contactForm,
        'nameFilterForm': nameForm,
        'vaStatusForm': vaForm,
        "dataPeople": dataPeople,
        "dataDogs": dataDogs,
    }
    return render(request, "dogGallery.html", context)


def show_home(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    # get only active dogs
    dataDogs = [dog for dog in dataDogs if dog['fields']['status'] == 'Active']
    dataDogs = dataDogs[:6]
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataPeople = set(Dog.objects.values_list(
        "va_name_bg", "va_name_eng").exclude(va_name_eng=""))

    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    date_pk = last_month.strftime("%Y-%b")

    donation_stories = DonationStory.objects.filter(date=last_month)
    genderForm = genderFilterForm()
    nameForm = DogFilterForm()
    vaForm = vaStatusForm()
    contactForm = ContactForm()
    adoptForm = AdoptForm()
    # dataDogs2 = Dog.objects.filter(status="Active")
    countDogs = Dog.objects.filter(status="Active").count(
    ) + Dog.objects.filter(status="Sick").count()
    countSick = Dog.objects.filter(status="Sick").count()
    # count the number of dogs that were adopted last year using adoption year field to filter
    countAdoptedLastYear = Dog.objects.filter(
        adoption_year=today.year-1).count()

    adopted = Dog.objects.filter(adoption_year=today.year-1)
    # filter away adopted for dogs where there is no adoption_pic_after_1
    adopted = adopted.exclude(adoption_pic_after_1="")
    adopted = adopted.order_by("?")[0]
    context = {
        "adoptedPuppy": adopted,
        "countDogs": countDogs,
        "countSick": countSick,
        "countAdoptedLastYear": countAdoptedLastYear,
        "donation_stories": donation_stories,
        'subscribeForm': renderCommon(request),
        "genderFilterForm": genderForm,
        "adoptForm": adoptForm,
        "contactForm": contactForm,
        'nameFilterForm': nameForm,
        'vaStatusForm': vaForm,
        "dataPeople": dataPeople,
        "dataDogs": dataDogs,
        "date_pk": date_pk,
        "dataNoticeBoard": dataNoticeBoard
    }
    return render(request, "home.html", context)

# from django.views import View
# from django.core import serializers
# from .models import Dog, NoticeBoard

# tdd = test driven dev
# pytest
# test_request = {...}
# def test_show_home(test_request):
#   ans = show_home(test_request)
#   assert ans == {this is what expect}


def show_infirmary(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataAbout = serializers.serialize(
        'python', About.objects.all().order_by("order"))
    context = {
        'subscribeForm': renderCommon(request),
        "dataDogs": dataDogs,
        "dataAbout": dataAbout,
        "dataNoticeBoard": dataNoticeBoard
    }
    return render(request, "clinic.html", context)


def show_about(request):
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataAbout = serializers.serialize(
        'python', About.objects.all().order_by("order"))

    context = {
        'subscribeForm': renderCommon(request),
        "dataAbout": dataAbout,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "ourstory.html", context)


def show_adoptions(request):
    dataDogs = serializers.serialize(
        'python', Dog.objects.all().order_by("-adoption_year"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dogs = Dog.objects.all().filter(adoption_year__gt=0).order_by("-adoption_year")
    # Get only adoption_year from Dog model
    years = set(dogs.values_list("adoption_year", flat=True))
    # Sort years in descending order
    years = sorted(years, reverse=True)

    context = {
        "years": years,
        "dogs": dogs,
        'subscribeForm': renderCommon(request),
        "dataAdoptions": dataDogs,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "adoptions.html", context)


def show_donations(request):
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("?"))
    dataAbout = serializers.serialize(
        'python', About.objects.all().order_by("order"))

    dataPeople = set(Dog.objects.values_list(
        "va_name_bg", "va_name_eng").exclude(va_name_eng=""))

    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)

    month = last_month.strftime('%m')
    year = last_month.strftime('%Y')
    last_month_cl = "("+month + " - " + year + ")"

    dataDonations = set(Donation.objects.values_list(
        "person_name_bg", "person_name_eng").filter(date=last_month).order_by("person_name_bg"))

    context = {
        'subscribeForm': renderCommon(request),
        "last_month": last_month,
        "dataPeople": dataPeople,
        "dataAbout": dataAbout,
        "month": last_month_cl,
        "dataDonations": dataDonations,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "donations.html", context)
