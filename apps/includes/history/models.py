from ipaddress import ip_address
from tkinter.tix import Balloon
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class History(models.Model):
    registration_code = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    type_register = models.CharField(max_length=150, null=True, blank=True)
    system_operation = models.CharField(max_length=150, null=True, blank=True)
    ip_address  = models.CharField(max_length=20, null=True, blank=True)
    browser = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField()