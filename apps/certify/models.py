from django.db import models
from apps.business.models import business

# Create your models here.
from apps.vehicles.models import vehicles
from apps.people.models import people

# Create your models here.
class types_services(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    class Meta:
        db_table = 'Type of service'
        ordering = ['name']
        verbose_name_plural = 'Tipo de servicio'

    def __str__(self):
        return self.name

class scopes(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(null=True)
    class Meta:
        db_table = 'scopes'
        ordering = ['name']
        verbose_name_plural = 'Alcances'

    def __str__(self):
        return self.name

class citv(models.Model):
    id = models.CharField(primary_key=True, max_length=25)
    Registration_date =models.DateTimeField()
    expiration_date = models.DateTimeField()
    inspection_result = models.BooleanField()
    comment = models.TextField()
    Type_of_inspection = models.CharField(max_length=150)
    file = models.FileField(upload_to="citv", null=True)
    vehicle = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    type_service = models.ForeignKey(types_services, null=True, blank=True, on_delete=models.CASCADE)
    scope = models.ForeignKey(scopes, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'citv'
        ordering = ['Type_of_inspection']
        verbose_name_plural = 'CITV'

    def __str__(self):
        return self.Type_of_inspection

class categories(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True, null=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'category'
        ordering = ['name']
        verbose_name_plural = 'Categoria'

    def __srt__(self):
        return self.name

class soat(models.Model):
    policy = models.CharField(max_length=15)
    certify = models.CharField(max_length=15, null=True)
    insurance_company = models.ForeignKey(business, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField()
    registration_date = models.DateField()
    date_expiry = models.DateField()
    category = models.ForeignKey(categories, null=True, blank=True, on_delete=models.CASCADE)
    vin_serie = models.CharField(max_length=15)
    insured = models.CharField(max_length=150, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    file = models.FileField(upload_to="soat", null=True)
    vehicles = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    owners = models.ManyToManyField(people, blank=True)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'SOAT'
        ordering = ['-insurance_company']
        verbose_name_plural = 'SOAT'

    def __srt__(self):
        return self.insurance_company

# Create your models here.
class src(models.Model):
    name = models.CharField(max_length=150)
    registration_date = models.DateTimeField()
    date_expiry = models.DateTimeField()
    file = models.FileField(upload_to="src", null=True)
    vehicles = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    delete_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'SRC'
        ordering = ['name']
        verbose_name_plural = 'SRC'

    def __srt__(self):
        return self.name

# Create your models here.
class svct(models.Model):
    name = models.CharField(max_length=150)
    registration_date = models.DateTimeField()
    date_expiry = models.DateTimeField()
    file = models.FileField(upload_to="svct", null=True)
    vehicles = models.ForeignKey(vehicles, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,null=True)
    delete_at = models.DateTimeField(auto_now=True,null=True, blank=True)

    class Meta:
        db_table = 'SVCT'
        ordering = ['name']
        verbose_name_plural = 'SVCT'

    def __srt__(self):
        return self.name