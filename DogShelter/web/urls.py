from django.urls import path

from DogShelter.web import views

urlpatterns = (
    path("", views.show_home, name="home"),
    path("ourstory/", views.show_about, name="about"),
    path("donations/", views.show_donations, name="donations"),
    path("adoptions/", views.show_adoptions, name="adoptions"),
    path("clinic/", views.show_infirmary, name="infirmary"),
    path('dogGallery/<int:pk>/', views.show_dog.as_view(), name='dog_profile'),
    # path("sign_up/", views.SignUpView.as_view(), name="sign_up"),
    path('donations/history/<str:date_pk>/',
         views.show_donation_story.as_view(), name='donation_monthly'),
    path("dogGallery/", views.show_all_dogs, name="all_dogs"),
)
