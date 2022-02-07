# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.vehicles.views import VehiclesViews

urlpatterns = [
    path('', VehiclesViews.index, name='vehicles.index'),
]