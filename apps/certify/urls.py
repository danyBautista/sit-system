# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.certify import views

urlpatterns = [
    path('', views.CertifyView.index, name='certify.index'),
    path('list/<str:type>', views.CertifyList.index, name='certify.list'),
    path('create/soat/<str:key>', views.createAPI_SOAT.as_view(), name='certify.create.soat'),
    path('create/citv/<str:key>', views.createAPI_CITV.as_view(), name='certify.create.citv'),
    path('create/src/<str:key>', views.createAPI_SRC.as_view(), name='certify.create.src'),
    path('create/svct/<str:key>', views.createAPI_SVCT.as_view(), name='certify.create.svct'),
    path('select/', views.ValidateLegal, name='certify.select'),
    path('query/<int:pk>', views.CertifyQuery.as_view(), name='certify.query'),
    path('api/select/soat/', views.API_ValidateLegalSOAT.as_view(), name='select.soat'),
    path('api/select/citv/', views.API_ValidateLegalCITV.as_view(), name='select.citv'),
    path('api/select/src/', views.API_ValidateLegalSRC.as_view(), name='select.src'),
    path('api/select/svct/', views.API_ValidateLegalSVCT.as_view(), name='select.srct')
]