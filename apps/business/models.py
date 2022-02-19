from django.db import models
from apps.control.models import economic_activities
from apps.control.models import geographic_location
# Create your models here.

class business(models.Model):
    ruc = models.CharField(max_length=11, primary_key=True, unique=True)
    business_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=150, blank=True)
    webpage = models.CharField(max_length=150, blank=True)
    registration_date = models.DateTimeField(null=True)
    opening_date = models.DateField(null=True)
    logo_small_path = models.ImageField(upload_to="bussines", null=True)
    logo_large_path = models.ImageField(upload_to="bussines", null=True)
    business_description = models.TextField(null=True)
    geographic_location = models.ForeignKey(geographic_location, null=True, blank=True, on_delete=models.CASCADE)
    economic_activitie = models.ManyToManyField(economic_activities)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'business'
        ordering = ['business_name']
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.business_name