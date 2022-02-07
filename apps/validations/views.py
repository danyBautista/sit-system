# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
class ValidationsView(HttpResponse): 
    def index(request):
        context = {'segment': 'validation'}
        html_template = loader.get_template('validations/index.html')
        return HttpResponse(html_template.render(context, request))