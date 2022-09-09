from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index.as_view(), name='inspections'),
    path('search', search.as_view(), name='inspections.search')
]