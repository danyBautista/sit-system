# Generated by Django 4.0.1 on 2022-02-22 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_alter_economic_activities_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='economic_activities',
            options={'ordering': ['heading'], 'verbose_name_plural': 'Actividades economicas'},
        ),
        migrations.AlterModelOptions(
            name='geographic_location',
            options={'ordering': ['id'], 'verbose_name_plural': 'ubicacion geografica'},
        ),
        migrations.AlterModelOptions(
            name='marial_status',
            options={'ordering': ['id'], 'verbose_name_plural': 'Estado Civil'},
        ),
        migrations.AlterModelOptions(
            name='sex',
            options={'ordering': ['id'], 'verbose_name_plural': 'sexo'},
        ),
    ]
