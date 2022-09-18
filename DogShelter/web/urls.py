from django.urls import path

from DogShelter.web import views

urlpatterns = (
    path("", views.show_home, name="home"),
    path("about/", views.show_about, name="about"),
    path("donations/", views.show_donations, name="donations"),
    path("adoptions/", views.show_adoptions, name="adoptions"),
    path("giftadoption/", views.show_giftAdoption, name="giftadoption"),
)
