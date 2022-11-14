from django.contrib import admin


from DogShelter.web.models import Dog, NoticeBoard, People, About, Donations
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog

@admin.register(Dog)
class Dog(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["id","name_eng","person","status","story_bg"]
    list_filter = ["person","status", "story_eng","story_bg"]

@admin.register(NoticeBoard)
class NoticeBoard(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(People)
class People(admin.ModelAdmin):
    readonly_fields = ('id',)

@admin.register(About)
class About(admin.ModelAdmin):
    readonly_fields = ('id',)

@admin.register(Donations)
class Donations(admin.ModelAdmin):
    readonly_fields = ('id',)
