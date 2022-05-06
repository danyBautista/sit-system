# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path
from apps.reports import views

urlpatterns = [
    path('', views.IndexView, name='report.index')
]