from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib import messages

from apps.includes.sidebar.models import Sidebar
# Create your views here.

@login_required(login_url='/login/')
class RegisterView(HttpResponse):
    def index(request, pk):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones', 'pk' : pk}
        html_template = loader.get_template('procedure/create.html')
        return HttpResponse(html_template.render(context, request))