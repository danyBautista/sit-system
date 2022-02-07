# Generated by Django 4.0.1 on 2022-02-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='src',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('registration_date', models.DateTimeField()),
                ('date_expiry', models.DateTimeField()),
                ('file', models.FilePathField()),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('vehicles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles')),
            ],
            options={
                'verbose_name_plural': 'SRC',
                'db_table': 'SRC',
                'ordering': ['name'],
            },
        ),
    ]
