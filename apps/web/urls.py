# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.web import views

urlpatterns = [

    # The home page
    path('', views.WebPageIndex.as_view(), name='web.index'),
]
