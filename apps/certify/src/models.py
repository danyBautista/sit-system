from django.db import models

from apps.vehicles.models import vehicles

# Create your models here.
class src(models.Model):
    name = models.CharField(max_length=150)
    registration_date = models.DateTimeField()
    date_expiry = models.DateTimeField()
    file = models.FilePathField()
    vehicles = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'SRC'
        ordering = ['name']
        verbose_name_plural = 'SRC'

    def __srt__(self):
        return self.name