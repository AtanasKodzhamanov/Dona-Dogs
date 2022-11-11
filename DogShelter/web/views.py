from django.core import serializers
from django.shortcuts import render

from DogShelter.web.models import Dog, NoticeBoard, Adoptions, People, Donations, About

# Create your views here.

def show_home(request):  # dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
    dataNoticeBoard = serializers.serialize('python', NoticeBoard.objects.all().order_by("order"))
    dataPeople = serializers.serialize('python', People.objects.all())
    
    context={
        "dataPeople": dataPeople,
        "dataDogs": dataDogs,
        "dataNoticeBoard": dataNoticeBoard
    }
    
    return render(request, "index.html", context)


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

#dataDogs = serializers.serialize('python', Dog.objects.all().order_by("?"))
#dataPeople = serializers.serialize('python', People.objects.all().order_by("?"))



#for instance in dataDogs:
    #print(instance)
    #print(instance["fields"]["person"])
    #id=instance["fields"]["person"]
    #print(dataPeople["id"==id]["fields"]["person_name_eng"])
    #print(dataPeople)
 