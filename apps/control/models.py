from django.db import models

# Create your models here.
class economic_activities(models.Model):
    title = models.IntegerField()
    category = models.IntegerField()
    sub_category = models.IntegerField()
    heading = models.CharField(max_length=150)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'economic_activities'
        ordering = ['title']
        verbose_name_plural = 'Economic_activities'

    def __unicode__(self):
        return self.title

class geographic_location(models.Model):
    id = models.CharField(max_length=6, primary_key=True, unique=True)
    department = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    captial = models.CharField(max_length=150)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'geographic_location'
        ordering = ['id']
        verbose_name_plural = 'geographic_location'

    def __unicode__(self):
        return self.id

class sex(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'sex'
        ordering = ['id']
        verbose_name_plural = 'sex'

    def __str__(self):
        return '{}'.format(self.name)

class marial_status(models.Model):
    name = models.CharField(max_length=50, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'marial_status'
        ordering = ['id']
        verbose_name_plural = 'marial_status'

    def __str__(self):
        return '{}'.format(self.name)