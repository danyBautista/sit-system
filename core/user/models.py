
from django.db import models

from crum import get_current_request

from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from apps.administration.models import profiles
from core.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class User(AbstractUser):
    user_photo_path = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True, null=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    profile = models.ForeignKey(profiles, null=True, blank=True, on_delete=models.CASCADE)

    def get_photo_path(self):
        if self.user_photo_path:
            return '{}{}'.format(MEDIA_URL, self.user_photo_path)
        return '{}{}'.format(STATIC_URL, 'assets/img/user.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['user_photo_path'] = self.get_photo_path()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        return item

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass