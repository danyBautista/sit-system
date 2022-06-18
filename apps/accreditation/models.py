from django.db import models
from apps.business.models import business
from apps.validations.models import routes
from apps.vehicles.models import  vehicles, types
# Create your models here.

class accreditation_type(models.Model):
    COLOR_FILED = (
        ('success', 'success'),
        ('danger', 'danger'),
        ('warning', 'warning'),
        ('dark', 'dark'),
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('grey', 'grey')
    )
    ICON_FILED = (
        ('verified_user','verified_user'),
        ('health_and_safety','verified_user'),
        ('security','verified_user'),
        ('shield','verified_user'),
        ('policy','verified_user'),
        ('privacy_tip','verified_user'),
        ('gpp_maybe','verified_user'),
        ('gpp_bad','verified_user'),
        ('safety_check','verified_user'),
        ('add_moderator','verified_user'),
        ('remove_moderator','verified_user')
    )
    name = models.TextField(max_length=150, unique=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    color = models.TextField(max_length=50, choices=COLOR_FILED, null=True, blank=True)
    icon = models.TextField(max_length=60, choices=ICON_FILED, null=True, blank=True)
    status = models.BooleanField(null=True)

    def __str__(self):
        return self.name

class accreditation(models.Model):
    STATUSFIELD = (
        ('CUMPLE', 'CUMPLE'),
        ('NO CUMPLE', 'NO CUMPLE'),
        ('PENDIENTE', 'PENDIENTE')
    )
    STATUS = (
        ('ACREDITADO', 'ACREDITADO'),
        ('PENDIENTE', 'PENDIENTE'),
        ('RETIRADO', 'RETIRADO')
    )
    plate = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    route = models.ForeignKey(routes, null=True, blank=True, on_delete=models.CASCADE)
    legal_requirements = models.CharField(max_length=20, choices=STATUSFIELD)
    technical_requirements = models.CharField(max_length=20, choices=STATUSFIELD)
    mechanical_inspection = models.CharField(max_length=20, choices=STATUSFIELD)
    insurance = models.CharField(max_length=20, choices=STATUSFIELD)
    accreditation_card = models.BooleanField()
    year_of_production = models.CharField(max_length=4,null=True, blank=True)
    typology = models.ForeignKey(types, null=True, blank=True, on_delete=models.CASCADE)
    permit_number = models.CharField(max_length=5, null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    bussines = models.ForeignKey(business, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS)
    type = models.ForeignKey(accreditation_type, null=True, blank=True, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True, blank=True)
