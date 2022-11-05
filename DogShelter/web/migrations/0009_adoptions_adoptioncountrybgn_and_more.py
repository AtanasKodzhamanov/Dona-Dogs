# Generated by Django 4.1 on 2022-11-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_noticeboard_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptions',
            name='AdoptionCountryBGN',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='adoptions',
            name='AdoptionCountryENG',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='adoptions',
            name='DogNameBG',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='adoptions',
            name='DogNameENG',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
