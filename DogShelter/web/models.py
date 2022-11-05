from django.db import models
from django.utils.timezone import now
# Create your models here.


class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y", "N", "Unknown")]
    GENDER = [(x, x) for x in ("F", "M")]

    def __str__(self):
        return self.nameENG

    # Fields(Columns)
    nameENG = models.CharField(
        max_length=NAME_MAX_LENGTH,
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
        max_length=300
    )

    pic3 = models.URLField(
        blank=True,
        max_length=300
    )

    pic4 = models.URLField(
        blank=True,
        max_length=300
    )

    pic5 = models.URLField(
        blank=True,
        max_length=300
    )

    virtual_adopter = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        blank=True
    )

    story_ENG = models.TextField(
        blank=True,
        default=""
    )
    story_BG = models.TextField(
        blank=True,
        default=""
    )


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


class Adoptions(models.Model):

    class Meta: 
        verbose_name_plural = "Adoptions"

    NAME_MAX_LENGTH = 60

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
