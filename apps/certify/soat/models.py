
from django.db import models
from apps.owner.models import owner
from apps.vehicles.models import models, vehicles

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'category'
        ordering = ['name']
        verbose_name_plural = 'category'

    def __srt__(self):
        return self.name

class soat(models.Model):
    policy = models.CharField(max_length=8)
    certify = models.CharField(max_length=10)
    insurance_company = models.CharField(max_length = 150)
    number = models.IntegerField()
    registration_date = models.DateTimeField()
    date_expiry = models.DateTimeField()
    category = models.ForeignKey(categories, null=True, blank=True, on_delete=models.CASCADE)
    vin_serie = models.CharField(max_length=15)
    insured = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    file = models.FilePathField()
    vehicles = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    owners = models.ManyToManyField(owner)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'SOAT'
        ordering = ['-insurance_company']
        verbose_name_plural = 'SOAT'

    def __srt__(self):
        return self.insurance_company

