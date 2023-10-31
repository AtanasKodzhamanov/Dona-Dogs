from django.urls import path
from django.views.i18n import JavaScriptCatalog

from DogShelter.web import views


urlpatterns = (
    path("handler404", views.handler404),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript_catalog"),
    path("", views.HomeView.as_view(), name="home"),
    path("ourstory/", views.AboutView.as_view(), name="about"),
    path("donations/", views.DonationsView.as_view(), name="donations"),
    path("adoptions/", views.AdoptionsView.as_view(), name="adoptions"),
    path("clinic/", views.ClinicView.as_view(), name="infirmary"),
    path("dogGallery/<int:pk>/", views.DogProfileView.as_view(), name="dog_profile"),
    path(
        "donations/history/<str:date_pk>/",
        views.DonationStoryView.as_view(),
        name="donation_monthly",
    ),
    path("dogGallery/", views.GalleryView.as_view(), name="all_dogs"),
    path("contact/", views.contact_form_view, name="contact"),
)
