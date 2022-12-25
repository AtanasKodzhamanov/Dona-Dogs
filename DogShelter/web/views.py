import datetime
from django import views
from django.core import serializers
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
import django.utils.translation
from DogShelter.web.forms import SubscribeForm, ContactForm, AdoptForm, DogFilterForm, vaStatusForm, genderFilterForm
from DogShelter.web.models import Dog, DonationStory, NoticeBoard, About, Donation
from django.utils.translation import  activate
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
    model = [DonationStory, Donation]
    template_name = "donationStory.html"

    def get_queryset(self):
        date_pk = self.kwargs['date_pk']
        return DonationStory.objects.filter(date_pk=date_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_pk'] = self.kwargs['date_pk']

        donation_names = Donation.objects.all()
        donations = DonationStory.objects.all()
        context['donation_names'] = donation_names
        context['donations'] = donations
        context['subscribeForm'] = renderCommon(self.request)
        return context

class show_dog(DetailView):
    model = Dog
    template_name = "dog.html"
    queryset = Dog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscribeForm'] = renderCommon(self.request)
        return context
    
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
    #dataDogs2 = Dog.objects.filter(status="Active")
    countDogs = Dog.objects.filter(status="Active").count() + Dog.objects.filter(status="Sick").count()
    countSick = Dog.objects.filter(status="Sick").count()
    # count the number of dogs that were adopted this year using adoption year field to filter 
    countAdoptedLastYear = Dog.objects.filter(adoption_year=today.year).count()

    context = {
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
        "date_pk":date_pk,
        "dataNoticeBoard": dataNoticeBoard
    }
    return render(request, "index.html", context)

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

    context = {
        'subscribeForm': renderCommon(request),
        "dataDogs": dataDogs,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "infirmary.html", context)

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
    return render(request, "about.html", context)


def show_adoptions(request):
    dataDogs = serializers.serialize(
        'python', Dog.objects.all().order_by("-adoption_year"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))

    context = {
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

# def show_giftAdoption(request):
#     dataNoticeBoard = serializers.serialize(
#         'python', NoticeBoard.objects.all().order_by("order"))
#     dataPeople = serializers.serialize(
#         'python', Dog.objects.all().exclude(va_name_eng=""))

#     context = {
#         'subscribeForm': renderCommon(request),
#         "dataPeople": dataPeople,
#         "dataNoticeBoard": dataNoticeBoard
#     }

#     return render(request, "giftadoption.html", context)

