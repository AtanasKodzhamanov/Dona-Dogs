# Generated by Django 4.1.3 on 2022-11-14 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0043_rename_donation_pic_donations_donation_pic_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='web.people'),
        ),
    ]