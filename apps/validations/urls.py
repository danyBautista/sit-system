# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.validations.views import ListView, SearchView, ValidateVehicle, ProcedureRegister, ProcedureCreate, ContractCreate, authorizaitonCreate, ValidateCreate

urlpatterns = [
    path('', ListView.index, name='validate.index'),
    path('create', ValidateCreate.as_view, name='validate.create'),
    path('search/', SearchView.index, name='validate.search'),
    path('select/', ValidateVehicle.index, name='validate.val'),
    path('procedure/<str:pk>', ProcedureRegister.index, name='procedure.register'),
    path('api/route/create/', ProcedureCreate.as_view(), name='procedure.create'),
    path('api/contract/create/', ContractCreate.as_view(), name='procedure.contract.create'),
    path('api/authorization/create/', authorizaitonCreate.as_view(), name='procedure.authorization.create')
]