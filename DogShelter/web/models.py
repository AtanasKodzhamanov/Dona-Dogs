from django.db import models
from django.utils.timezone import now
# Create your models here.

class People(models.Model):

    NAME_MAX_LENGTH = 60
    
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
    
    email_address=models.EmailField(
        blank=True,
        default=""
    )
    
    
class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y", "N", "Unknown")]
    GENDER = [(x, x) for x in ("F", "M")]
    STATUS = [(x, x) for x in ("Active", "Dead","Adopted")]

    def __str__(self):
        return self.name_eng

    person=models.ForeignKey(People, on_delete=models.DO_NOTHING,default=1, verbose_name='Virtual Adopter')
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
    
    active = models.CharField(
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

    person=models.ForeignKey(People, on_delete=models.DO_NOTHING,default=1)
    
    donation_pic = models.URLField(
        null=True,
        max_length=300
    )

    donation_amount = models.FloatField(
        default=0
    )

    donation_currency = models.CharField(
        max_length=CURRENCY_MAX_LENGTH,
        default=""
    )

    donation_description_eng = models.TextField(
        blank=True,
        default=""
    )

    donation_description_bg = models.TextField(
        blank=True,
        default=""
    )

    donation_date = models.DateField(
        
    )
    
class NoticeBoard(models.Model):

    class Meta: 
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return self.note_eng
      
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

class Adoptions(models.Model):

    class Meta: 
        verbose_name_plural = "Adoptions"

    NAME_MAX_LENGTH = 60
    
    person=models.ForeignKey(People, on_delete=models.DO_NOTHING,default=1)
    
    def __str__(self):
        return self.dog_name_eng
    
    dog_name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,    
        null=True
    )
    dog_name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )
    
    adoption_country_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )
    
    adoption_country_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    adoption_description_eng = models.TextField(
        blank=True,
        default=""
    )

    adoption_description_bg = models.TextField(
        blank=True,
        default=""
    )

    adoption_pic_before = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    adoption_pic_after_1 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    adoption_pic_after_2 = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )

    adoption_video = models.URLField(
        max_length=300,
        blank=True,
        default=""
    )