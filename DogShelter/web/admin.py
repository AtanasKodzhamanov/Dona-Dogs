from django.contrib import admin


from DogShelter.web.models import Dog
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog


@admin.register(Dog)
class Dog(admin.ModelAdmin):
    pass