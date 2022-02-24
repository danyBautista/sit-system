from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse

from apps.includes.sidebar.models import Sidebar
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    sidebar = Sidebar.objects.all()
    title = Sidebar.objects.get(id=8)

    context = {'segment': 'modules', 'sidebars': sidebar, 'title': title, 'page':'Modulos'}
    Http_template = loader.get_template('business/index.html')
    return HttpResponse(Http_template.render(context, request))