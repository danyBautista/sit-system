# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.urls import path

from apps.reports.views import HomeIndex, AccreditationReports

urlpatterns = [
    path('', HomeIndex.index, name='report.index'),
    path('accreditation/<str:tp>', AccreditationReports.as_view(), name='report.accreditation')
]