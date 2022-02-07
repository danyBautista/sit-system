from django.db import models
from apps import business
from apps.business.models import business
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
        verbose_name_plural = 'type'

    def __srt__(self):
        return self.name

class vehicles(models.Model):
    plate = models.CharField(max_length=8, primary_key=True, unique=True)
    mark = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year_of_production = models.DateField()
    longitude = models.IntegerField()
    height = models.IntegerField()
    broad = models.IntegerField()
    service_door = models.IntegerField()
    type_id = models.ForeignKey(types, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=150)
    comment = models.TextField()
    business_id = models.ForeignKey(business, null=True, blank=True, on_delete=models.CASCADE)
    terms = models.CharField(max_length=8)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'Vehicles'
        ordering = ['plate']
        verbose_name_plural = 'vehicle'

    def __str__(self):
        return self.model

