from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from django.contrib import messages

from apps.vehicles.models import vehicles
from apps.certify.models import soat
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
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        if request.method == "POST":
            pk = request.POST.get('plate', '')
            vehicle = vehicles.objects.filter(plate = pk, status = True).first()
            SOAT = soat.objects.filter(vehicles=pk, status=True).first()

        if SOAT:
            msg_soat = {'class': 'bg-gradient-success', 'icon': 'check', 'message': 'No existe SOAT', 'data': SOAT}
        else:
            msg_soat = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe SOAT'}

        context =   {
                        'segment': 'validate',
                        'sidebars': sidebar,
                        'title': title,
                        'page':'Validaciones',
                        'unit': vehicle,
                        'soat' : msg_soat
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