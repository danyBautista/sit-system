# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from core.user.models import User
# Create your models here.

class Consulting(models.Model):
    key_register = models.CharField(max_length=15, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date_query = models.DateTimeField(auto_now_add=True)
    status_query = models.BooleanField()