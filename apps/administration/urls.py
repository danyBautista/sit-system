# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.administration import views

urlpatterns = [
    path('', views.AdminIndex.index, name='admin.index'),
    path('user/', views.UserIndex.as_view(), name='admin.user'),
    path('user/create/', views.UserCreate.as_view(), name='admin.user.create'),
    path('user/api/search', views.UserApiList.as_view(), name='admin.user.api.search')
]