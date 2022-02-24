# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.vehicles.views import VehiclesViews, VehiclesListAPIView, VehiclesCreate

urlpatterns = [
    path('', VehiclesViews.index, name='vehicles.index'),
    path('create', VehiclesCreate.index, name='vehicles.create'),

    path('api/search/', VehiclesListAPIView.as_view(), name='vehicle.search')
]