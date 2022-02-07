# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from apps.vehicles.models import vehicles
# Create your views here.
class VehiclesViews(HttpResponse):
    def index(request):
        context = {'segment': 'vehicles'}
        html_template = loader.get_template('vehicles/index.html')
        return HttpResponse(html_template.render(context, request))