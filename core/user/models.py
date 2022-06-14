from django.db import models
from django.contrib.auth.models import AbstractUser

from core.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class User(AbstractUser):
    user_photo_path = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True, null=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)

    def get_photo_path(self):
        if self.user_photo_path:
            return '{}{}'.format(MEDIA_URL, self.user_photo_path)
        return '{}{}'.format(STATIC_URL, 'assets/img/user.png')
