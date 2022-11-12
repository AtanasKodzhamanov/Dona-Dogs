# Generated by Django 4.1.3 on 2022-11-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0040_rename_active_dog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='adoption_pic_after_1',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='dog',
            name='adoption_pic_after_2',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='dog',
            name='adoption_pic_after_3',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
    ]