# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.business import views

urlpatterns = [
    path('', views.ListView, name='business.index'),
    path('create/', views.BusinessCreate.index, name='business.create'),

    path('api/create/', views.businessAPICreate.as_view(), name="busines.register"),
]