# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.includes.sidebar.views import SidebarList

urlpatterns = [
    path('sidebar', SidebarList.as_view(), name='sidebar.index'),
]