from django.contrib import admin
from .models import citv, scopes, types_services
# Register your models here.

admin.site.register(citv)
admin.site.register(scopes)
admin.site.register(types_services)