# Generated by Django 2.2.8 on 2020-02-16 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotels_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='slug',
        ),
    ]
