from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from apps.business.forms import BusinessForm
from apps.business.models import business
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')

# Create your views here.
class CertifyView(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=6)
        context = {'segment': 'certify', 'sidebars': sidebar, 'title': title, 'page':'Certificados'}
        html_template = loader.get_template('certify/index.html')
        return HttpResponse(html_template.render(context, request))
