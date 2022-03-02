# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.validations.views import ListView, SearchView, ValidateVehicle

urlpatterns = [
    path('', ListView.index, name='validate.index'),
    path('search/', SearchView.index, name='validate.search'),
    path('select/', ValidateVehicle.index, name='validate.val'),
]