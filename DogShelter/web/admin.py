from django.contrib import admin


from DogShelter.web.models import Dog, NoticeBoard, About, Donation
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog


@admin.register(Dog)
class Dog(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["name_eng",  "status", "va_name_eng"]
    list_filter = ["status", ("story_bg", admin.EmptyFieldListFilter),
                   ("story_eng", admin.EmptyFieldListFilter)]


@admin.register(NoticeBoard)
class NoticeBoard(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["location", "note_bg"]


@admin.register(About)
class About(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(Donation)
class Donation(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["person_name_eng", "date"]
