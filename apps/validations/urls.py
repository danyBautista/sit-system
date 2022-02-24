# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.validations.views import ListView, CreateView

urlpatterns = [
    path('', ListView.index, name='validate.index'),
    path('create/', CreateView.index, name='validate.create'),
]