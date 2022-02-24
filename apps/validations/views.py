from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')
# Create your views here.
class ListView(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones'}
        html_template = loader.get_template('validations/index.html')
        return HttpResponse(html_template.render(context, request))

class CreateView(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones'}
        html_template = loader.get_template('validations/create.html')
        return HttpResponse(html_template.render(context, request))