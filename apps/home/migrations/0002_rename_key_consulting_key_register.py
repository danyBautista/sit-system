# Generated by Django 4.0.1 on 2022-06-23 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulting',
            old_name='key',
            new_name='key_register',
        ),
    ]