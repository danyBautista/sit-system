# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.certify import views

urlpatterns = [
    path('', views.CertifyView, name='certify.index'),
    path('create/soat', views.createAPI_SOAT.as_view(), name='certify.create.soat'),
    path('create/citv', views.createAPI_CITV.as_view(), name='certify.create.citv'),
    path('select/', views.ValidateLegal, name='certify.select')
]