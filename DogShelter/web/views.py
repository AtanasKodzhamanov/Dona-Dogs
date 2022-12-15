import datetime
from django.core import serializers
from django.shortcuts import render
import django.utils.translation
from DogShelter.web.models import Dog, NoticeBoard, About, Donation
from .forms import DogFilterForm, vaStatusForm, SubscribeForm

# Create your views here.

lang = django.utils.translation.get_language()

def show_home(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))
    dataPeople = set(Dog.objects.values_list(
        "va_name_bg", "va_name_eng").exclude(va_name_eng=""))

    nameForm = DogFilterForm()
    vaForm = vaStatusForm()
    subscribeForm = SubscribeForm()
    #dataDogs2 = Dog.objects.filter(status="Active")

    context = {
        'SubscribeForm': subscribeForm,
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
        "dataAbout": dataAbout,
        "dataNoticeBoard": dataNoticeBoard,
        "lang": lang
    }
    return render(request, "about.html", context)


def show_adoptions(request):
    dataDogs = serializers.serialize(
        'python', Dog.objects.all().order_by("-adoption_year"))
    dataNoticeBoard = serializers.serialize(
        'python', NoticeBoard.objects.all().order_by("order"))

    context = {
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
    #last_month_cl = last_month.strftime('%B')
   # last_month_cl = "".format(last_month.strftime('%m'))
    month = last_month.strftime('%m')
    year = last_month.strftime('%Y')
    last_month_cl = "("+month + " - " + year + ")"

    dataDonations = set(Donation.objects.values_list(
        "person_name_bg", "person_name_eng").filter(date=last_month).order_by("person_name_bg"))

    context = {
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

    # return list of virtual adopters

    context = {
        "dataPeople": dataPeople,
        "dataNoticeBoard": dataNoticeBoard
    }

    return render(request, "giftadoption.html", context)

