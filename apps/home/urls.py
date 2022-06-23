# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.DashboardView.as_view(), name='home'),
    path('query/api/select/<str:key>', views.ConsultingAPIView.as_view(), name='home.query.select'),
    path('query/api/create/', views.ConsultingAPICreate.as_view(), name='home.query.create'),
    path('query/<str:key>', views.ConsultingView.as_view(), name='home.query'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
