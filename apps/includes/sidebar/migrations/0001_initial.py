# Generated by Django 4.0.1 on 2022-02-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('route', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=20)),
                ('group', models.CharField(max_length=4)),
                ('segment', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('sub_menu', models.BigIntegerField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
