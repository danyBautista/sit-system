# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path

from apps.reports.views import HomeIndex

urlpatterns = [
    path('', HomeIndex.index, name='report.index')
]