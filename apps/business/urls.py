# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.business.views import ListView, BusinessCreate, businessAPICreate, businessAPIList, BusinessUpdate

urlpatterns = [
    path('', ListView.index, name='business.index'),
    path('create/', BusinessCreate.as_view(), name='business.create'),
    path('update/<str:pk>', BusinessUpdate.as_view(), name='business.update'),
    path('api/search/', businessAPIList.as_view(), name='business.search'),
    path('api/create/', businessAPICreate.as_view(), name="busines.register"),
]