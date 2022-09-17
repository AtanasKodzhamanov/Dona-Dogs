from django.db import models

# Create your models here.

class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y","N", "Unknown")]

    # Fields(Columns)
    nameENG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=True
    )
    nameBG = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    monthly_upkeep = models.IntegerField()

    diseases= models.CharField(
        max_length=7,
        choices=Options,
        default=""
    )

    gender= models.CharField(
        max_length=7,
        choices=Options,
        default=""
    )

    profile_pic = models.URLField(
        null=True,
        max_length = 300
    )

    virtual_adopter= models.CharField(
        max_length=NAME_MAX_LENGTH,
        default=""
    )

    arrival_date = models.DateTimeField(
        default=""
    )

    story_ENG = models.TextField(
        blank=True,
        default=""
    )
    story_BG = models.TextField(
        blank=True,
        default=""
    )

