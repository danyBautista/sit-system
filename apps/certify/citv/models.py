from tabnanny import verbose
from django.db import models

from apps.vehicles.models import vehicles

# Create your models here.
class types_services(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    class Meta:
        db_table = 'Type of service'
        ordering = ['name']
        verbose_name_plural = 'Tipo de servicio'

    def __str__(self):
        return self.name

class scopes(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    class Meta:
        db_table = 'scopes'
        ordering = ['name']
        verbose_name_plural = 'Alcances'

    def __str__(self):
        return self.name

class citv(models.Model):
    id = models.CharField(primary_key=True, max_length=21)
    Registration_date =models.DateTimeField()
    expiration_date = models.DateTimeField()
    inspection_result = models.BooleanField()
    comment = models.TextField()
    Type_of_inspection = models.CharField(max_length=150)
    file = models.FileField(upload_to="citv", null=True)
    vehicle = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    type_service = models.ForeignKey(types_services, null=True, blank=True, on_delete=models.CASCADE)
    scope = models.ForeignKey(scopes, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'citv'
        ordering = ['Type_of_inspection']
        verbose_name_plural = 'CITV'

    def __str__(self):
        return self.Type_of_inspection