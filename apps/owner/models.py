

from django.db import models
from apps.people.models import people
from apps.vehicles.models import vehicles
# Create your models here.
class owner(models.Model):
    people_id = models.ForeignKey(people, blank=True, null=True, on_delete=models.CASCADE)
    vehicles_id = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class meta:
        db_table = 'owner'
        ordering = ['status']
        verbose_name_plural = 'owner'

    def _unicode_(self):
        return self.status