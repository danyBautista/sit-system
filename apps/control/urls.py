# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.control import views

urlpatterns = [
    path('api/ecoact/search/', views.EconomicActivitieList.as_view(), name='ecoact.search'),
]