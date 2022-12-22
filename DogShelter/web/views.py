import datetime
from django import views
from django.core import serializers
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
import django.utils.translation
from DogShelter.web.forms import SubscribeForm, ContactForm, AdoptForm, DogFilterForm, vaStatusForm, genderFilterForm
from DogShelter.web.models import Dog, NoticeBoard, About, Donation
from django.utils.translation import  activate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView

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

class show_dog(DetailView):
    model = Dog
    template_name = "dog.html"
    # pk_url_kwarg = 'name_eng'
    queryset = Dog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscribeForm'] = renderCommon(self.request)
        return context
    



def show_home(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataPeople = set(Dog.objects.values_list(
        "va_name_bg", "va_name_eng").exclude(va_name_eng=""))
    
    genderForm = genderFilterForm()
    nameForm = DogFilterForm()
    vaForm = vaStatusForm()
    contactForm = ContactForm()
    adoptForm = AdoptForm()
    #dataDogs2 = Dog.objects.filter(status="Active")

    context = {
        'subscribeForm': renderCommon(request),
        "genderFilterForm": genderForm,
        "adoptForm": adoptForm,
        "contactForm": contactForm,
        'nameFilterForm': nameForm,
        'vaStatusForm': vaForm,
        "dataPeople": dataPeople,
        "dataDogs": dataDogs,
        "dataNoticeBoard": dataNoticeBoard
    }
    return render(request, "index.html", context)

# from django.views import View
# from django.core import serializers
# from .models import Dog, NoticeBoard

# class ShowHome(View):
#     def dispatch(request, *args, **kwargs):
#         dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
#         dataNoticeBoard = serializers.serialize(
#             'python', NoticeBoard.objects.all().order_by("order"))
#         dataPeople = set(Dog.objects.values_list(
#             "va_name_bg", "va_name_eng").exclude(va_name_eng=""))

#         #dataDogs2 = Dog.objects.filter(status="Active")

#         context = {
#             "dataPeople": dataPeople,
#             "dataDogs": dataDogs,
#             "dataNoticeBoard": dataNoticeBoard
#         }
#         return self.render_to_response(context)

# urlpatterns = [
#     path('', ShowHome.as_view(), name='home'),
# ]

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

def show_giftAdoption(request):
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataPeople = serializers.serialize(
        'python', Dog.objects.all().exclude(va_name_eng=""))

    context = {
        'subscribeForm': renderCommon(request),
        "dataPeople": dataPeople,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "giftadoption.html", context)

