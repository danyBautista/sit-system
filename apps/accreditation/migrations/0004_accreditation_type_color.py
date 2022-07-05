# Generated by Django 4.0.1 on 2022-06-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation', '0003_alter_accreditation_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='accreditation_type',
            name='color',
            field=models.TextField(blank=True, choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('dark', 'dark'), ('primary', 'primary'), ('secondary', 'secondary'), ('grey', 'grey')], max_length=50, null=True),
        ),
    ]