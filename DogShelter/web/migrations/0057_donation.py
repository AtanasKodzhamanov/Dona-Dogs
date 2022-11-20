# Generated by Django 4.1.3 on 2022-11-20 01:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0056_delete_donations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date(2022, 10, 31))),
                ('person_name_eng', models.CharField(max_length=60, null=True)),
                ('person_name_bg', models.CharField(max_length=60, null=True)),
            ],
        ),
    ]