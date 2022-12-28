from datetime import timezone
import datetime
from django import forms
from django.contrib import admin
from DogShelter.web import models


from DogShelter.web.models import Dog, NoticeBoard, About, Donation, NewsletterSubscriber, DonationStory
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog


@admin.register(Dog)
class Dog(admin.ModelAdmin):
    list_display = ["name_eng", "id", "status", "va_name_eng", "profile_pic", "pic_2", "pic_3",
                    "pic_4", "pic_5", "adoption_pic_after_1", "adoption_pic_after_2", "adoption_pic_after_3"]
    list_filter = ["status", ("story_bg", admin.EmptyFieldListFilter),
                   ("story_eng", admin.EmptyFieldListFilter)]


@admin.register(NoticeBoard)
class NoticeBoard(admin.ModelAdmin):
    list_display = ["location", "note_bg", "note_pic_1", "note_pic_2"]
    list_display_links = ["note_pic_1", "note_pic_2"]


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ["section_title_bg", "section_title_eng"]
    readonly_fields = ('id',)


@admin.register(Donation)
class Donation(admin.ModelAdmin):
    list_display = ["person_name_eng", "date"]
    list_per_page = 100


@admin.register(DonationStory)
class DonationStory(admin.ModelAdmin):
    list_display = ["donation_text_bg", "donation_text_eng", "date"]


@admin.register(NewsletterSubscriber)
class NewsletterSubscriber(admin.ModelAdmin):
    list_display = ["email", "name"]
