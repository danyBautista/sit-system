# Generated by Django 4.0.1 on 2022-02-22 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_alter_business_opening_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'ordering': ['business_name'], 'verbose_name_plural': 'Empresas'},
        ),
    ]
