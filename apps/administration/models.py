from django.db import models

class profiles(models.Model):
    profile_name = models.CharField(max_length=250, blank=True)
    route = models.CharField(max_length=250)
    status = models.BooleanField()
    
    def __str__(self):
        return self.profile_name