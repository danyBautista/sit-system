# Generated by Django 4.0.1 on 2022-06-15 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='accreditation_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='accreditation',
            name='enabled',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accreditation',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accreditation.accreditation_type'),
        ),
    ]
