# Generated by Django 2.2.8 on 2020-02-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20200214_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
