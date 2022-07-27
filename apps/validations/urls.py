# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path, re_path
from apps.validations.views import ListView, SearchView, ValidateVehicle, procedureAPIList, ValidationForm , ProcedureRegister, ProcedureCreate, ContractCreate, authorizaitonCreate, ValidateCreate, YearAntiquity, ProcedureSearchAPIView, ProcedureView,authorizationCreate, substitutionCreate

urlpatterns = [
    path('', ListView.index, name='validate.index'),
    path('create/', ValidateCreate.as_view(), name='validate.create.proceeding'),
    path('search/', SearchView.index, name='validate.search'),
    path('view/<str:pk>', ProcedureView.index, name='procedure.view'),
    path('select/<str:pk>', ValidateVehicle.index, name='validate.val'),
    path('procedure/<str:pk>', ValidationForm.as_view(), name='procedure.register'),
    path('authorization/create', authorizationCreate.as_view(), name='procedure.authorization.create'),
    path('api/list/vehicle/', procedureAPIList.as_view(), name='procedure.list'),
    path('api/route/create/', ProcedureCreate.as_view(), name='procedure.create'),
    path('api/contract/create/<str:plate>', ContractCreate.as_view(), name='procedure.contract.create'),
    path('api/authorization/create/', authorizaitonCreate.as_view(), name='procedure.api.authorization.create'),
    path('api/substitution/create/', substitutionCreate.as_view(), name='procedure.api.substitution.create'),
    path('api/control/year/', YearAntiquity.as_view(), name="year.antiquity"),
    path('api/search/', ProcedureSearchAPIView.as_view(), name='procedure.search')
]