from django.contrib import admin
from .models import economic_activities, sex, geographic_location, marial_status
# Register your models here.
class EcoActivAdmin(admin.ModelAdmin):
    search_fields = ('heading',)
    list_display = ['title', 'category', 'sub_category', 'heading']

admin.site.register(economic_activities, EcoActivAdmin)
admin.site.register(sex)
admin.site.register(geographic_location)
admin.site.register(marial_status)