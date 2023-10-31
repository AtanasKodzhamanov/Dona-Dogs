from django.contrib import admin
from DogShelter.web.models import (
    Dog,
    NoticeBoard,
    LongPost,
    Donation,
    NewsletterSubscriber,
    DonationStory,
    ContactFormModel,
)

# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name_eng",
        "status",
        "va_name_eng",
        "profile_pic",
        "pic_2",
        "pic_3",
        "pic_4",
        "pic_5",
        "adoption_pic_after_1",
        "adoption_pic_after_2",
        "adoption_pic_after_3",
    ]
    list_filter = [
        "status",
        ("story_bg", admin.EmptyFieldListFilter),
        ("story_eng", admin.EmptyFieldListFilter),
    ]
    list_display_links = ["id"]


@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ["id", "location", "note_bg", "note_pic_1", "note_pic_2"]
    list_display_links = ["id"]


@admin.register(LongPost)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["id", "location", "section_title_bg", "section_title_eng"]
    list_display_links = ["id"]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ["id", "person_name_eng", "date"]
    list_display_links = ["id"]
    list_per_page = 100


@admin.register(DonationStory)
class DonationStoryAdmin(admin.ModelAdmin):
    list_display = ["id", "donation_text_bg", "donation_text_eng", "date"]
    list_display_links = ["id"]


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "name"]
    list_display_links = ["id"]


@admin.register(ContactFormModel)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
