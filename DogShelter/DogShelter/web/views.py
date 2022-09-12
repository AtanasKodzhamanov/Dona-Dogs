from django.shortcuts import render

# Create your views here.
def show_home(request): #dashboard
    return render(request, "index.html")

def show_about (request):
    return render(request, "about.html")

def show_adoptions (request):
    return render(request, "adoptions.html")

def show_donations (request):
    return render(request, "donations.html")

def show_giftAdoption (request):    
    return render(request, "giftadoption.html")