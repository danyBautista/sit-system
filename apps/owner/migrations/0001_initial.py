# Generated by Django 4.0.1 on 2022-06-10 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('people_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.people')),
                ('vehicles_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles')),
            ],
        ),
    ]
