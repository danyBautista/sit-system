# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.people import views

urlpatterns = [
    path('', views.PeopleIndex.as_view(), name='people.index'),
    path('create/', views.PeopleCreate.as_view(), name='people.createView'),
    path('update/<str:pk>', views.PeopleUpdate.as_view(), name='people.updateView'),
    path('view/<key_id>/', views.view, name='people.view'),
    path('api/search/', views.PeopleListAPIView.as_view(), name='people.search'),
    path('api/search/dni/', views.PeopleSearchDNI.as_view(), name='people.search'),
    path('api/create/', views.PeopleCreateAPI.as_view(), name='people.create'),
    path('api/select/<pk>/', views.SelectAPIView.as_view(), name="people.select"),
    path('api/update/<pk>', views.PeopleUpdateAPIView.as_view(), name="people.update"),
    path('delete/<str:pk>', views.PeopleDeleteSoft.as_view(), name='people.partialUpdate')
]