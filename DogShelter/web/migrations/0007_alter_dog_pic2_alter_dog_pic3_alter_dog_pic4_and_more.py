# Generated by Django 4.1 on 2022-11-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_adoptions_options_alter_donations_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='pic2',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pic3',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pic4',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pic5',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
    ]