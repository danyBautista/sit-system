from django.db import models
from apps import business
from apps.business.models import business
from apps.people.models import people
# Create your models here.
class types(models.Model):
    name = models.CharField(max_length=100, default="No Comment Added")
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'type'
        ordering = ['name']
        verbose_name_plural = 'Tipo'

    def __str__(self):
        return self.name

class vehicles(models.Model):
    plate = models.CharField(max_length=8, primary_key=True, unique=True)
    mark = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year_of_production = models.IntegerField()
    longitude = models.DecimalField(max_digits=4, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    broad = models.DecimalField(max_digits=4, decimal_places=2)
    service_door = models.IntegerField()
    type = models.ForeignKey(types, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=150)
    comment = models.TextField()
    business = models.ForeignKey(business, null=True, blank=True, on_delete=models.CASCADE)
    users = models.ManyToManyField(people, blank=True)
    terms = models.CharField(max_length=8)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Vehicles'
        ordering = ['plate']
        verbose_name_plural = 'Vehiculos'

    def __str__(self):
        return self.model

