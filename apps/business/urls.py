# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.business.views import BusinessIndex, BusinessCreate, businessAPICreate, businessAPIList, BusinessUpdate, BusinessView, BusinessDeleteSoft

urlpatterns = [
    path('', BusinessIndex.as_view(), name='business.index'),
    path('create/', BusinessCreate.as_view(), name='business.create'),
    path('update/<str:pk>', BusinessUpdate.as_view(), name='business.update'),
    path('view/<str:pk>', BusinessView.index, name='business.view'),
    path('delete/<str:pk>', BusinessDeleteSoft.as_view(), name='business.delete'),
    path('api/search/', businessAPIList.as_view(), name='business.search'),
    path('api/create/', businessAPICreate.as_view(), name="busines.register"),
]