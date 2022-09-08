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
    path('user/update/<int:pk>', views.UserUpdate.as_view(), name='admin.user.update'),
    path('user/api/search', views.UserApiList.as_view(), name='admin.user.api.search'),
    path('user/change/group/<int:pk>', views.UserChangeGroup.as_view(), name='user.change.group'),
    path('user/chage/password/', views.UserPasswordChangeView.as_view(), name='user.change.password'),
    path('profile/', views.ProfileIndex.as_view(), name='profile.index'),
    path('profile/create', views.ProfileCreate.as_view(), name='profile.create')
]