from django.contrib import admin
from .models import soat, citv, src, svct, scopes, categories, types_services
# Register your models here.
admin.site.register(soat)
admin.site.register(citv)
admin.site.register(src)
admin.site.register(svct)
admin.site.register(scopes)
admin.site.register(categories)
admin.site.register(types_services)