from django.urls import path

from DogShelter.web import views


urlpatterns = (
    path("", views.show_home, name="home"),
    path("about/", views.show_about, name="about"),
    path("donations/", views.show_donations, name="donations"),
    path("adoptions/", views.show_adoptions, name="adoptions"),
    path("giftadoption/", views.show_giftAdoption, name="giftadoption"),
    path("infirmary/", views.show_infirmary, name="infirmary"),
    # path('dogs/<str:name>/', views.show_dog.as_view(), name='dog'),
    path('dogs/<int:pk>/', views.show_dog.as_view(), name='dogs'),
    # path("sign_up/", views.SignUpView.as_view(), name="sign_up"),
    path('donations/history/<str:date>/', views.show_donation_story.as_view(), name='donationStory'),
)
