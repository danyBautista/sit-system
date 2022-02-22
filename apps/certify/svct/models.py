from django.db import models

from apps.vehicles.models import vehicles

# Create your models here.
class svct(models.Model):
    name = models.CharField(max_length=150)
    registration_date = models.DateTimeField()
    date_expiry = models.DateTimeField()
    file = models.FileField(upload_to="people", null=True)
    vehicles = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,null=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'SVCT'
        ordering = ['name']
        verbose_name_plural = 'SVCT'

    def __srt__(self):
        return self.name