# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.business import views

urlpatterns = [
    path('', views.index, name='business.index'),
]