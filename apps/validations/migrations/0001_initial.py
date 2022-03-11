# Generated by Django 4.0.1 on 2022-03-10 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0005_rename_users_vehicles_owners'),
        ('certify', '0003_alter_citv_delete_at_alter_src_delete_at_and_more'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='authorization_documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('enabled', models.CharField(choices=[(1, 'Aceptado'), (2, 'Rechazado'), (3, 'Observado')], default=1, max_length=30)),
                ('file', models.FileField(blank=True, null=True, upload_to='authorizacion_doc')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='binding_contracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('registration_date', models.DateField()),
                ('due_date', models.DateField()),
                ('document', models.FileField(blank=True, null=True, upload_to='binding_contratcs')),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proceedings', models.CharField(max_length=6)),
                ('check_date', models.DateField()),
                ('score', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('RECHASADO', 'Rechasado'), ('OBSERVADO', 'Observado')], default='OBSERVADO', max_length=9)),
                ('property_card', models.BooleanField()),
                ('seniority_period', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('RECHASADO', 'Rechasado'), ('OBSERVADO', 'Observado')], default='OBSERVADO', max_length=9)),
                ('soat_status', models.CharField(choices=[('VIGENTE', 'vigente'), ('NO VIGENTE', 'No vigente'), ('INDETERMINADO', 'Indeterminado')], default='INDETERMINADO', max_length=13)),
                ('citv_status', models.CharField(choices=[('VIGENTE', 'vigente'), ('NO VIGENTE', 'No vigente'), ('INDETERMINADO', 'Indeterminado')], default='INDETERMINADO', max_length=13)),
                ('src_status', models.CharField(choices=[('VIGENTE', 'vigente'), ('NO VIGENTE', 'No vigente'), ('INDETERMINADO', 'Indeterminado')], default='INDETERMINADO', max_length=13)),
                ('svct_status', models.CharField(choices=[('VIGENTE', 'vigente'), ('NO VIGENTE', 'No vigente'), ('INDETERMINADO', 'Indeterminado')], default='INDETERMINADO', max_length=13)),
                ('RRPP_Newsletter', models.BooleanField()),
                ('bonding_contract', models.BooleanField()),
                ('enabled', models.CharField(choices=[('ACEPTADO', 'Aceptado'), ('RECHASADO', 'Rechasado'), ('OBSERVADO', 'Observado')], default='OBSERVADO', max_length=9)),
                ('vehicle_authorization', models.BooleanField()),
                ('check_sistran', models.BooleanField()),
                ('due_date', models.DateField()),
                ('status', models.BooleanField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(auto_now=True, null=True)),
                ('authorization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='validations.authorization_documents')),
                ('citv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certify.citv')),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='validations.binding_contracts')),
                ('license_plate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles')),
                ('owner', models.ManyToManyField(to='people.people')),
            ],
            options={
                'verbose_name_plural': 'Tramites',
                'db_table': 'procedure',
                'ordering': ['proceedings'],
            },
        ),
        migrations.CreateModel(
            name='routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=6)),
                ('concession', models.CharField(choices=[('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'), ('C11', 'C11')], default='1', max_length=10)),
                ('short_name', models.CharField(max_length=50, null=True)),
                ('road', models.TextField(null=True)),
                ('status', models.BooleanField()),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('delete_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'route',
                'db_table': 'route',
                'ordering': ['route'],
            },
        ),
        migrations.CreateModel(
            name='vehicle_replacement_process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informative_ticket', models.BooleanField()),
                ('vehicle_autorizacion', models.BooleanField()),
                ('status', models.BooleanField()),
                ('plate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles')),
                ('procedure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='validations.procedure')),
            ],
        ),
        migrations.AddField(
            model_name='procedure',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='validations.routes'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='soat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certify.soat'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='src',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certify.src'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='svct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certify.svct'),
        ),
    ]
