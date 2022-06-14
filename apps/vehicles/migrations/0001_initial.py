# Generated by Django 4.0.1 on 2022-06-10 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Comment Added', max_length=100)),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tipo',
                'db_table': 'type',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='vehicles',
            fields=[
                ('plate', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('mark', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('year_of_production', models.IntegerField()),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=4)),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('broad', models.DecimalField(decimal_places=2, max_digits=4)),
                ('service_door', models.IntegerField()),
                ('category', models.CharField(max_length=150)),
                ('comment', models.TextField()),
                ('terms', models.CharField(max_length=8)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(blank=True, null=True)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.business')),
                ('owners', models.ManyToManyField(blank=True, to='people.people')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.types')),
            ],
            options={
                'verbose_name_plural': 'Vehiculos',
                'db_table': 'Vehicles',
                'ordering': ['plate'],
            },
        ),
    ]
