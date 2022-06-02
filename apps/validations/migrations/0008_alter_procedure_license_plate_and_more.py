# Generated by Django 4.0.1 on 2022-05-22 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_rename_users_vehicles_owners'),
        ('validations', '0007_alter_procedure_year_proceeding_vehicle_substitution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='license_plate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='year_proceeding',
            field=models.CharField(max_length=4),
        ),
    ]