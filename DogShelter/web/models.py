from django.db import models

# Create your models here.

class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y","N", "Unknown")]

    # Fields(Columns)
    nameENG = models.CharField(
        max_length=NAME_MAX_LENGTH
    )
    nameBG = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    monthly_upkeep = models.IntegerField()

    diseases= models.CharField(
        max_length=7,
        choices=Options
    )

    gender= models.CharField(
        max_length=7,
        choices=Options
    )

    profile_pic = models.URLField(
        max_length = 300
    )

    virtual_adopter= models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    arrival_date = models.DateTimeField(
    )

    story_ENG = models.TextField(
        null=True,
        blank=True,
    )
    story_BG = models.TextField(
        null=True,
        blank=True,
    )

