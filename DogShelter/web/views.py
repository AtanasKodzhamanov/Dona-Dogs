from django.core import serializers
from django.shortcuts import render

from DogShelter.web.models import Dog, NoticeBoard, Adoptions

# Create your views here.


def show_home(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataNoticeBoard = serializers.serialize('python', NoticeBoard.objects.all().order_by("order"))
    return render(request, "index.html", {"dataDogs": dataDogs, "dataNoticeBoard": dataNoticeBoard})


def show_about(request):
    return render(request, "about.html")


def show_adoptions(request):
    dataAdoptions = serializers.serialize('python', Adoptions.objects.all().order_by("?"))
    return render(request, "adoptions.html", {"dataAdoptions": dataAdoptions})


def show_donations(request):
    return render(request, "donations.html")


def show_giftAdoption(request):
    return render(request, "giftadoption.html")


#dataDogs = serializers.serialize('python', Dog.objects.all())
#dataNoticeBoard = serializers.serialize('python', NoticeBoard.objects.all())
#print(dataDogs)

# for instance in dataDogs:
#    print("INSTANCE")
#   print(instance)
#  print(instance["fields"]["nameENG"])


    