from django.db import models

from apps.vehicles.models import vehicles
# Create your models here.

class routes(models.Model):
    CONCESSIONS = (
        (1,'C1'),(2,'C2'),(3,'C3'),(4,'C4'),(5,'C5'),(6,'C6'),(7,'C7'),
        (8,'C8'),(9,'C9'),(10,'C10'),(11,'C11'),
    )
    route = models.CharField(max_length=6)
    concession = models.CharField(max_length=10, choices=CONCESSIONS, default=1)
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
        return self.route

class binding_contracts(models.Model):
    code = models.CharField(max_length=6)
    registration_date = models.DateField()
    due_date = models.DateField()
    document = models.FileField('binding_contratcs', null=True, blank=True)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class authorization_documents(models.Model):
    SKILLED = (
        (1, 'Aceptado'),
        (2, 'Rechazado'),
        (3, 'Observado')
    )
    code = models.CharField(max_length=6)
    enabled = models.CharField(max_length=30, choices=SKILLED, default=1)
    status = models.BooleanField()

class procedure(models.Model):
    ANCIENT_PERIOD = (
        (1, 'Aceptado'),
        (2, 'Rechazado'),
        (3, 'Observado')
    )
    proceedings = models.CharField(max_length=6)
    license_plate = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    check_date = models.DateField(auto_now_add=True)
    qualification = models.CharField(max_length=30, choices=ANCIENT_PERIOD, default=1)
    id_route = models.ForeignKey(routes, null=True, blank=True, on_delete=models.CASCADE)
    ancient_period = models.CharField(max_length=30, choices=ANCIENT_PERIOD, default=1)
    property_card = models.BooleanField()
    RRPP_Newsletter = models.CharField(max_length=2)
    contract = models.ForeignKey(binding_contracts, null=True, blank=True, on_delete=models.CASCADE)
    bonding = models.BooleanField()
    due_date = models.DateField()
    status = models.BooleanField()
    authorization = models.ForeignKey(authorization_documents, blank=True, null=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'procedure'
        ordering = ['proceedings']
        verbose_name_plural = 'Tramites'

    def __str__(self):
        return self.proceedings