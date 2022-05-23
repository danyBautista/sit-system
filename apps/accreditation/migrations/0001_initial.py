# Generated by Django 4.0.1 on 2022-05-22 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('validations', '0007_alter_procedure_year_proceeding_vehicle_substitution_and_more'),
        ('vehicles', '0005_rename_users_vehicles_owners'),
        ('business', '0003_alter_business_logo_large_path_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='accreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_requirements', models.CharField(choices=[('CUMPLE', 'CUMPLE'), ('NO CUMPLE', 'NO CUMPLE'), ('PENDIENTE', 'PENDIENTE')], max_length=20)),
                ('technical_requirements', models.CharField(choices=[('CUMPLE', 'CUMPLE'), ('NO CUMPLE', 'NO CUMPLE'), ('PENDIENTE', 'PENDIENTE')], max_length=20)),
                ('mechanical_inspection', models.CharField(choices=[('CUMPLE', 'CUMPLE'), ('NO CUMPLE', 'NO CUMPLE'), ('PENDIENTE', 'PENDIENTE')], max_length=20)),
                ('insurance', models.CharField(choices=[('CUMPLE', 'CUMPLE'), ('NO CUMPLE', 'NO CUMPLE'), ('PENDIENTE', 'PENDIENTE')], max_length=20)),
                ('accreditation_card', models.BooleanField()),
                ('year_of_production', models.CharField(blank=True, max_length=4, null=True)),
                ('permit_number', models.CharField(blank=True, max_length=5, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ACREDITADO', 'ACREDITADO'), ('PENDIENTE', 'PENDIENTE'), ('RETIRADO', 'RETIRADO')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(blank=True, null=True)),
                ('bussines', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.business')),
                ('plate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles')),
                ('route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='validations.routes')),
                ('typology', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.types')),
            ],
        ),
    ]
