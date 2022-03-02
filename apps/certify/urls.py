# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.certify import views

urlpatterns = [
    path('', views.CertifyView, name='certify.index'),

    path('select/', views.ValidateLegal, name='certify.select')
]