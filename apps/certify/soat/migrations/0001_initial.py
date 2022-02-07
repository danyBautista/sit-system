# Generated by Django 4.0.1 on 2022-02-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'category',
                'db_table': 'category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='soat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=8)),
                ('certify', models.CharField(max_length=10)),
                ('insurance_company', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
                ('registration_date', models.DateTimeField()),
                ('date_expiry', models.DateTimeField()),
                ('vin_serie', models.CharField(max_length=15)),
                ('insured', models.CharField(max_length=150)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('file', models.FilePathField()),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='soat.categories')),
                ('owners', models.ManyToManyField(to='owner.owner')),
                ('vehicles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles')),
            ],
            options={
                'verbose_name_plural': 'SOAT',
                'db_table': 'SOAT',
                'ordering': ['-insurance_company'],
            },
        ),
    ]
