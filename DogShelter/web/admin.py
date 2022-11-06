from django.contrib import admin


from DogShelter.web.models import Adoptions, Dog, NoticeBoard, Donations, People
# Register your models here.


class PetInlineAdmin(admin.StackedInline):
    model = Dog

@admin.register(Dog)
class Dog(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ["id","name_eng","person"]
    list_filter = ["person","active"]

@admin.register(Adoptions)
class Adoptions(admin.ModelAdmin):
    readonly_fields = ('id',)

@admin.register(NoticeBoard)
class NoticeBoard(admin.ModelAdmin):
    readonly_fields = ('id',)

@admin.register(Donations)
class Donations(admin.ModelAdmin):
    readonly_fields = ('id',)

@admin.register(People)
class People(admin.ModelAdmin):
    readonly_fields = ('id',)


