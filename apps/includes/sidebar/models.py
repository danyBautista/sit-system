from django.db import models

# Create your models here.


class Sidebar(models.Model):
    name = models.CharField(max_length=50)
    route = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField()
    icon = models.CharField(max_length=20)
    group = models.CharField(max_length=4)
    segment = models.CharField(max_length=30)
    status = models.BooleanField()
    sub_menu = models.BigIntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class meta:
        db_table = 'sidebar'
        ordering = ['-name']
        verbose_name_plural = 'sidebar'

    def _unicode_(self):
        return self.name