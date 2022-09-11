from django.urls import path

from DogShelter.web import views 

urlpatterns=(
    path("",views.show_home, name="home"),
    path("about/",views.show_about, name="about"),
)