# Generated by Django 4.1.2 on 2022-12-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0080_donationstory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationstory',
            name='date_pk',
            field=models.CharField(blank=True, editable=False, max_length=8),
        ),
    ]