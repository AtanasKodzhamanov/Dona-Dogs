from django.db import models
from django.forms import CharField, EmailField
from django.utils.timezone import now
from django.template.defaultfilters import slugify
import datetime


class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y", "N", "Unknown")]
    GENDER = [(x, x) for x in ("F", "M")]
    STATUS = [(x, x) for x in ("Active", "Dead", "Adopted", "Sick")]

    def __str__(self):
        return self.name_eng

    # Fields(Columns)

    name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=True
    )
    name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    va_name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        blank=True
    )
    va_name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        blank=True
    )

    # Chronic
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

    pic_2 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    pic_3 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    pic_4 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    pic_5 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    # If alive, adopted or sick. If alive keep in the gallery, if adopted send put it inside the adoption page, if sick put at the top of the gallery.
    status = models.CharField(
        max_length=10,
        blank=True,
        choices=STATUS,
        default="Active"
    )

    story_eng = models.TextField(
        blank=True,
        default=""
    )
    story_bg = models.TextField(
        blank=True,
        default=""
    )

    arrival_year = models.IntegerField(
        blank=True,
        default=0
    )

    adoption_country_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        default=""
    )

    adoption_country_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        default=""
    )

    adoption_year = models.IntegerField(
        blank=True,
        default=0
    )

    adoption_pic_after_1 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    adoption_pic_after_2 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    adoption_pic_after_3 = models.URLField(
        blank=True,
        max_length=300,
        default=""
    )

    # slug = models.SlugField(
    #     null=False,
    #     blank=True
    # )

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.slug:
    #         self.slug = slugify(f"{self.name_eng}--{self.pk}")
    #     return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-pk',)


class NoticeBoard(models.Model):

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.note_eng

    LOCATION = [(x, x) for x in ("Gallery", "About", "Infirmery",
                                 "Adoptions", "Virtual", "Donations")]

    note_eng = models.TextField(
        blank=True,
        default=""
    )

    note_bg = models.TextField(
        blank=True,
        default=""
    )

    note_pic_1 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    note_pic_2 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    order = models.IntegerField(
        default=99
    )

    location = models.CharField(
        max_length=25,
        blank=True,
        choices=LOCATION,
        default="Gallery"
    )


class About(models.Model):

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.section_title_eng

    LOCATION = [(x, x) for x in ("Gallery", "About", "Infirmary",
                                 "Adoptions", "Virtual", "Donations")]

    location = models.CharField(
        max_length=25,
        blank=True,
        choices=LOCATION,
        default="Donations"
    )

    section_desc_eng = models.TextField(
        blank=True,
        default="Info coming soon..."
    )

    section_desc_bg = models.TextField(
        blank=True,
        default=""
    )

    about_pic_1 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_2 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_3 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_4 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_5 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_6 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_7 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_8 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_9 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    about_pic_10 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    order = models.IntegerField(
        default=99
    )

    section_title_eng = models.TextField(
        max_length=100,
        blank=True,
        default=""
    )

    section_title_bg = models.TextField(
        max_length=100,
        blank=True,
        default=""
    )


today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)


class Donation(models.Model):

    def __str__(self):
        return "--".format(self.person_name_eng, self.date)

    NAME_MAX_LENGTH = 60

    date = models.DateField(
        blank=True,
        default=last_month
    )

    person_name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=True
    )
    person_name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=True
    )

class NewsletterSubscriber(models.Model):
    email = EmailField(required=True, label='Email')
    name = CharField(required=True, label='Name')

class AdoptionForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    dog = models.CharField(max_length=255)