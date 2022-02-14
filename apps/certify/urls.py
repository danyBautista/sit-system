# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.certify.views import CertifyView

urlpatterns = [
    path('', CertifyView.index, name='certify.index'),
]