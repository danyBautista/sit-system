# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.models import User
from apps.includes.sidebar.models import Sidebar

# Create your views here.
class AdminIndex(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=2)
        user = User.objects.all()
        context = {'segment': 'administration', 'sidebars': sidebar, 'title': title, 'page':'Reportes', 'user' : user}
        html_template = loader.get_template('administration/index.html')
        return HttpResponse(html_template.render(context, request))

