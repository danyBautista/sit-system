# Generated by Django 4.0.1 on 2022-05-28 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_historicalpeople'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Historicalpeople',
        ),
    ]
