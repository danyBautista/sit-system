# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.people import views

urlpatterns = [
    path('', views.index, name='people.index'),
    path('view/<key_id>/', views.view, name='people.view')
]