# Generated by Django 4.0.1 on 2022-02-06 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marial_status',
            options={'ordering': ['id'], 'verbose_name_plural': 'marial_status'},
        ),
        migrations.AlterModelOptions(
            name='sex',
            options={'ordering': ['id'], 'verbose_name_plural': 'sex'},
        ),
    ]
