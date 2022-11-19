from django.db import models
from django.utils.timezone import now
from django.template.defaultfilters import slugify


class People(models.Model):

    NAME_MAX_LENGTH = 60

    CHOICES = [(x, x) for x in ("Y", "N")]

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.person_name_eng

    person_name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=True
    )
    person_name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    email_address = models.EmailField(
        blank=True,
        default=""
    )

    virtual_adopter = models.CharField(
        max_length=2,
        default="No",
        choices=CHOICES,
        blank=True
    )


class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y", "N", "Unknown")]
    GENDER = [(x, x) for x in ("F", "M")]
    STATUS = [(x, x) for x in ("Active", "Dead", "Adopted", "Sick")]

    def __str__(self):
        return self.name_eng

    person = models.ForeignKey(
        People, on_delete=models.DO_NOTHING, default=1, verbose_name='Virtual Adopter')
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


class Donations(models.Model):
    person = models.ForeignKey(
        People, on_delete=models.DO_NOTHING, default=1, verbose_name='Donator')

    year_month = models.DateField(
        blank=True,
        default=now
    )
