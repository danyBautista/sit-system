# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.business.views import ListView, BusinessCreate

urlpatterns = [
    path('', ListView.index, name='business.index'),
    path('create/', BusinessCreate.index, name='business.create'),
]