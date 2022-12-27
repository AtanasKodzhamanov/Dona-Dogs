# Generated by Django 4.1.2 on 2022-12-27 12:42

import DogShelter.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0085_delete_aboutphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='section_title_bg',
            field=models.TextField(help_text='Заглавие на секцията на Български.', max_length=100, validators=[DogShelter.web.validators.validate_bulgarian]),
        ),
        migrations.AlterField(
            model_name='about',
            name='section_title_eng',
            field=models.TextField(help_text='Заглавие на секцията на Английски.', max_length=100, validators=[DogShelter.web.validators.validate_english]),
        ),
    ]
