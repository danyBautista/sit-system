# Generated by Django 4.0.1 on 2022-03-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validations', '0005_authorization_documents_commnet_procedure_years_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedure',
            name='year_proceeding',
            field=models.CharField(default=2022, max_length=4),
        ),
        migrations.AlterField(
            model_name='routes',
            name='concession',
            field=models.CharField(choices=[('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'), ('C11', 'C11')], max_length=10),
        ),
    ]