from django.db import models
from apps.control.models import geographic_location, marial_status, sex
from apps.business.models import business
from core.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class people(models.Model):
    dni = models.CharField(max_length=8, primary_key=True, unique=True)
    name = models.CharField(max_length=80, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    user_photo_path = models.ImageField(upload_to="people", null=True)
    sex = models.ForeignKey(sex, null=True, blank=True, on_delete=models.CASCADE)
    profile_information = models.TextField(null=True)
    geographic_location = models.ForeignKey(geographic_location, null=True, blank=True, on_delete=models.CASCADE)
    marial_status = models.ForeignKey(marial_status, null=True, blank=True, on_delete=models.CASCADE)
    business_id = models.ForeignKey(business, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'people'
        ordering = ['name']
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name  + " " + self.first_name  + " " + self.last_name

    def get_image(self):
        if self.user_photo_path:
            return '{}{}'.format(MEDIA_URL, self.user_photo_path)
        return '{}{}'.format(STATIC_URL, 'assets/img/empty-300x240.jpg')