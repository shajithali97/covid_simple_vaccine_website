# Generated by Django 3.2.8 on 2021-11-15 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_vaccination_app', '0002_vaccinationbooking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccinationbooking',
            old_name='Place',
            new_name='place',
        ),
        migrations.RenameField(
            model_name='vaccinationbooking',
            old_name='User',
            new_name='user',
        ),
    ]