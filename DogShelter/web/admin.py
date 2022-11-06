from django.contrib import admin


from DogShelter.web.models import Adoptions, Dog, NoticeBoard, Donations, People
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog

@admin.register(Dog)
class Dog(admin.ModelAdmin):
    pass

@admin.register(Adoptions)
class Adoptions(admin.ModelAdmin):
    pass

@admin.register(NoticeBoard)
class NoticeBoard(admin.ModelAdmin):
    pass

@admin.register(Donations)
class Donations(admin.ModelAdmin):
    pass

@admin.register(People)
class People(admin.ModelAdmin):
    readonly_fields = ('id',)


