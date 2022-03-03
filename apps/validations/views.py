from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from django.contrib import messages

import datetime

from apps.vehicles.models import vehicles
from apps.certify.models import soat

from apps.certify.forms import SOATForm
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

class SearchView(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones'}
        html_template = loader.get_template('validations/search-plate.html')
        return HttpResponse(html_template.render(context, request))

class ValidateVehicle(HttpResponse):
    def index(request):
        msg_soat = dict
        now = datetime.datetime.now()
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        if request.method == "POST":
            pk = request.POST.get('plate', '')
            if pk == '':
                return redirect('validate.search')
            else:
                vehicle = vehicles.objects.filter(plate = pk, status = True).first()
                if vehicle:
                    SOAT = soat.objects.filter(vehicles=pk, status=True).first()
                else:
                    return redirect('vehicles.create')

        form_soat = SOATForm()
        if SOAT:
            msg_soat = {'class': 'bg-gradient-success', 'icon': 'check', 'message': SOAT.policy, 'data': SOAT}
        else:
            msg_soat = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe SOAT', 'data': SOAT}

        forms = {'SOAT_F': form_soat}
        context =   {
                        'segment': 'validate',
                        'sidebars': sidebar,
                        'title': title,
                        'page':'Validaciones',
                        'unit': vehicle,
                        'soat' : msg_soat,
                        'forms' : forms
                    }
        html_template = loader.get_template('validations/validate.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url='/login/')
# Create your views here.
class SelectView(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones'}
        html_template = loader.get_template('validations/select.html')
        return HttpResponse(html_template.render(context, request))