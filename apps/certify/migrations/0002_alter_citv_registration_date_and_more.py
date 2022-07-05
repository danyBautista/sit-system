# Generated by Django 4.0.1 on 2022-06-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citv',
            name='Registration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='citv',
            name='expiration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='citv',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='soat',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='src',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='svct',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='types_services',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]