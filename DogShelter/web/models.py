from django.db import models
from django.utils.timezone import now
# Create your models here.


class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y", "N", "Unknown")]
    GENDER = [(x, x) for x in ("F", "M")]
    Binary = [(x, x) for x in ("Yes", "No")]

    def __str__(self):
        return self.nameENG

    # Fields(Columns)
    nameENG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=True
    )
    nameBG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    monthly_upkeep = models.IntegerField(
        default=0
    )

    diseases = models.CharField(
        max_length=7,
        choices=Options,
        default=""
    )

    gender = models.CharField(
        max_length=7,
        choices=GENDER,
        default=""
    )

    profile_pic = models.URLField(
        null=True,
        max_length=300
    )

    pic2 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    pic3 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    pic4 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    pic5 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    virtual_adopter = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        blank=True
    )
    
    active = models.CharField(
        max_length=3,
        blank=True,
        choices=Binary,
        default="Yes"
    )

    story_ENG = models.TextField(
        blank=True,
        default=""
    )
    story_BG = models.TextField(
        blank=True,
        default=""
    )
    
    arrival_year=models.IntegerField(
        blank=True,
        default=0
    )
    
    class Meta:
        ordering = ('pk',)
    
class Donations(models.Model):

    class Meta: 
        verbose_name_plural = "Donations"

    NAME_MAX_LENGTH = 60
    CURRENCY_MAX_LENGTH = 3

    fullNameENG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=True
    )
    fullNameBG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    donation_pic = models.URLField(
        null=True,
        max_length=300
    )

    donation_amount = models.IntegerField(
        default=0
    )

    donation_currency = models.CharField(
        max_length=CURRENCY_MAX_LENGTH,
        default=""
    )

    donation_descriptionENG = models.TextField(
        blank=True,
        default=""
    )

    donation_descriptionBG = models.TextField(
        blank=True,
        default=""
    )

    donation_date = models.DateField(

    )


class NoticeBoard(models.Model):

    class Meta: 
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return self.noticeENG
   
    noticeENG = models.TextField(
        blank=True,
        default=""
    )

    noticeBG = models.TextField(
        blank=True,
        default=""
    )

    notice_pic1 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    notice_pic2 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )
    
    order = models.IntegerField(
        default=99
    )


class Adoptions(models.Model):

    class Meta: 
        verbose_name_plural = "Adoptions"

    NAME_MAX_LENGTH = 60

    DogNameENG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=True
    )
    DogNameBG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )
    
    AdoptionCountryENG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )
    
    AdoptionCountryBGN = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    adoption_descriptionENG = models.TextField(
        blank=True,
        default=""
    )

    adoption_descriptionBG = models.TextField(
        blank=True,
        default=""
    )

    adoption_pic_before = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    adoption_pic_after1 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    adoption_pic_after2 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    adoption_video = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )


class People(models.Model):

    NAME_MAX_LENGTH = 60
    
    class Meta: 
        verbose_name_plural = "People"

    person_name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=True
    )
    person_name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )