# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.validations.views import ValidationsView

urlpatterns = [
    path('', ValidationsView.index, name='validate_index'),
]