from django.shortcuts import render

from DogShelter.web.models import Dog

# Create your views here.
def show_home(request): #dashboard
    dataDogs = serializers.serialize('python', Dog.objects.all())
    return render(request, "index.html", {"dataDogs":dataDogs})

def show_about (request):
    return render(request, "about.html")

def show_adoptions (request):
    return render(request, "adoptions.html")

def show_donations (request):
    return render(request, "donations.html")

def show_giftAdoption (request):    
    return render(request, "giftadoption.html")



from django.core import serializers
dataDogs = serializers.serialize('python', Dog.objects.all())
print(dataDogs)

# for instance in dataDogs: 
 #    print("INSTANCE")
  #   print(instance)
   #  print(instance["fields"]["nameENG"])
    
  
