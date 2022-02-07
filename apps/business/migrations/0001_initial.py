# Generated by Django 4.0.1 on 2022-02-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='business',
            fields=[
                ('ruc', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('business_name', models.CharField(blank=True, max_length=150)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=150)),
                ('webpage', models.CharField(blank=True, max_length=150)),
                ('registration_date', models.DateTimeField()),
                ('opening_date', models.DateField()),
                ('logo_small_path', models.ImageField(upload_to='')),
                ('logo_large_path', models.ImageField(upload_to='')),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('economic_activitie', models.ManyToManyField(to='control.economic_activities')),
                ('geographic_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control.geographic_location')),
            ],
            options={
                'verbose_name_plural': 'business',
                'db_table': 'business',
                'ordering': ['business_name'],
            },
        ),
    ]