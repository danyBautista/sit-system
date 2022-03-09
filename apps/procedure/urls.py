# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path
from apps.procedure import views

urlpatterns = [
    path('register/<str:pk>', views.RegisterView, name='procedure.register')
]