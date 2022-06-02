from xmlrpc.client import boolean
from django.db import models
from datetime import datetime, date, timedelta

from apps.people.models import people
from apps.vehicles.models import vehicles
from apps.certify.models import soat, citv, src, svct

# Create your models here.

class routes(models.Model):
    CONCESSIONS = (
        ('C1', 'C1'),('C2','C2'),('C3','C3'),('C4','C4'),('C5','C5'),('C6','C6'),('C7','C7'),
        ('C8','C8'),('C9','C9'),('C10','C10'),('C11','C11'),
    )
    route = models.CharField(max_length=45)
    concession = models.CharField(max_length=10, choices=CONCESSIONS, blank=True, null=True)
    short_name = models.CharField(max_length=50, null=True)
    road = models.TextField(null=True)
    status = models.BooleanField()
    limit = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'route'
        ordering = ['route']
        verbose_name_plural = 'route'

    def __str__(self):
        return self.concession + " - " + self.route

class binding_contracts(models.Model):
    code = models.CharField(max_length=16)
    registration_date = models.DateField()
    due_date = models.DateField()
    document = models.FileField(upload_to='binding_contratcs', null=True, blank=True)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.code + " - " + str(self.registration_date)

class authorization_documents(models.Model):
    SKILLED = (
        (1, 'Aceptado'),
        (2, 'Rechazado'),
        (3, 'Observado')
    )
    code = models.CharField(max_length=30)
    enabled = models.CharField(max_length=30, choices=SKILLED, default=1)
    file = models.FileField(upload_to='authorizacion_doc', null=True, blank=True)
    status = models.BooleanField()
    commnet = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.code

class validation_tools(models.Model):
    years_antiquity = models.IntegerField()
    status_years = models.BooleanField()

    def __str__(self):
        return str(self.years_antiquity)

class vehicle_substitution(models.Model):
	sustitucion = models.BooleanField()
	exit_ticket = models.BooleanField()
	plate = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
	vehicle_authorization_document = models.BooleanField()
	file_authorization = models.FileField(upload_to='substitution', null=True, blank=True)


class procedure(models.Model):
    PROFILE = (
        ('ACEPTADO', 'Aceptado'),
        ('RECHAZADO', 'Rechazado'),
        ('OBSERVADO', 'Observado')
    )
    VALIDITY = (
        ('VIGENTE', 'vigente'),
        ('NO VIGENTE', 'No vigente'),
        ('INDETERMINADO', 'Indeterminado')
    )
    current_date = datetime.today()
    YEAR_CHOICES = [(r,r) for r in range(2000, datetime.today().year+1)]
    proceedings = models.CharField(max_length=6)
    year_proceeding = models.CharField(max_length=4)#, choices=YEAR_CHOICES, default=current_date.year)
    check_date = models.DateField()
    license_plate = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    route = models.ForeignKey(routes, null=True, blank=True, on_delete=models.CASCADE)
    score = models.CharField(max_length=9, choices=PROFILE)
    property_card = models.BooleanField()
    seniority_period = models.CharField(max_length=9, choices=PROFILE)
    soat = models.ForeignKey(soat, null=True, blank=True, on_delete=models.CASCADE)
    soat_status = models.CharField(max_length=13, choices=VALIDITY)
    citv = models.ForeignKey(citv, null=True, blank=True, on_delete=models.CASCADE)
    citv_status = models.CharField(max_length=13, choices=VALIDITY)
    src = models.ForeignKey(src, null=True, blank=True, on_delete=models.CASCADE)
    src_status = models.CharField(max_length=13, choices=VALIDITY)
    svct = models.ForeignKey(svct, null=True, blank=True, on_delete=models.CASCADE)
    svct_status = models.CharField(max_length=13, choices=VALIDITY)
    RRPP_Newsletter = models.BooleanField()
    owner = models.ManyToManyField(people)
    contract = models.ForeignKey(binding_contracts, null=True, blank=True, on_delete=models.CASCADE)
    bonding_contract =  models.BooleanField()
    enabled = models.CharField(max_length=9, choices=PROFILE)
    vehicle_authorization  =  models.BooleanField()
    check_sistran  =  models.BooleanField()
    due_date = models.DateField()
    status = models.BooleanField()
    authorization = models.ForeignKey(authorization_documents, blank=True, null=True, on_delete=models.CASCADE)
    years = models.ForeignKey(validation_tools, null=True, blank=True, on_delete=models.CASCADE)
    substitution = models.ForeignKey(vehicle_substitution, null=True, blank=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'procedure'
        ordering = ['proceedings']
        verbose_name_plural = 'Tramites'

    def __str__(self):
        return self.proceedings

class vehicle_replacement_process(models.Model):
    procedure = models.ForeignKey(procedure, null=True, blank=True, on_delete=models.CASCADE)
    plate = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    informative_ticket = models.BooleanField()
    vehicle_autorizacion = models.BooleanField()
    status = models.BooleanField()