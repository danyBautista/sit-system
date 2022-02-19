from django.contrib import admin
from .models import people
# Register your models here.

class peopleAdmin(admin.ModelAdmin):
    search_fields = ('dni', 'name', 'first_name', 'last_name')
    list_display = ['dni', 'name', 'first_name', 'last_name']

admin.site.register(people, peopleAdmin)