from django.db import models
from django.utils.timezone import now
# Create your models here.

class Dog(models.Model):

    NAME_MAX_LENGTH = 60

    Options = [(x, x) for x in ("Y","N", "Unknown")]
    GENDER =[(x, x) for x in ("F","M")]

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

    diseases= models.CharField(
        max_length=7,
        choices=Options,
        default=""
    )

    gender= models.CharField(
        max_length=7,
        choices=GENDER,
        default=""
    )

    profile_pic = models.URLField(
        null=True,
        max_length = 300
    )

    virtual_adopter= models.CharField(
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

