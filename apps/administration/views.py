# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from apps.includes.sidebar.models import Sidebar
# Create your views here.

@login_required(login_url="/login/")
def index(request): 
    users = User.objects.all()
    modules = Sidebar.objects.all()
    context = {'segment': 'administration', 'users': users, 'modules' : modules}
    html_template = loader.get_template('administration/index.html')
    return HttpResponse(html_template.render(context, request))