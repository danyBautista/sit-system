from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from rest_framework.response import Response

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
import datetime

from apps.vehicles.models import vehicles
from apps.certify.models import soat, citv, src, svct
from apps.validations.models import routes, procedure, validation_tools

from apps.certify.forms import SOATForm, CITVForm, SRCForm, SVCTForm
from apps.validations.forms import RoutesForm, ProcedureForm, SubstitutionForm

from .serializers import RouteSerializer, BindingContractsSerializer, AuthorizationDocumentSerializer, ValidationToolsSerializer, ProcedureSerializer
# Create your views here.


# Create your views here.
class ListView(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        procedures = procedure.objects.all()
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones', 'procedures' : procedures}
        html_template = loader.get_template('validations/index.html')
        return HttpResponse(html_template.render(context, request))

class ProcedureSearchAPIView(ListAPIView):
    queryset = procedure.objects.all()
    serializer_class = ProcedureSerializer
    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return procedure.objects.filter(proceedings__icontains = kword)

class SearchView(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones'}
        html_template = loader.get_template('validations/search-plate.html')
        return HttpResponse(html_template.render(context, request))

class ValidateVehicle(HttpResponse):
    @login_required(login_url='/login/')
    def index(request, pk):
        print(pk)
        msg_soat = dict
        now = datetime.datetime.now()
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)

        vehicle = vehicles.objects.filter(plate = pk, status = True).first()

        SOAT = soat.objects.filter(vehicles=pk, status=True).first()
        CITV = citv.objects.filter(vehicle=pk, status=True).first()
        SRC = src.objects.filter(vehicles=pk, status=True).first()
        SVCT = svct.objects.filter(vehicles=pk, status=True).first()

        form_soat = SOATForm()
        form_citv = CITVForm()
        form_src = SRCForm()
        form_svct = SVCTForm()

        if SOAT:
            msg_soat = {'class': 'bg-gradient-success', 'icon': 'check', 'message': SOAT.policy, 'data': SOAT}
        else:
            msg_soat = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe SOAT', 'data': SOAT}

        if CITV:
            msg_citv = {'class': 'bg-gradient-success', 'icon': 'check', 'message': CITV.id, 'data': CITV}
        else:
            msg_citv = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe CITV', 'data': CITV}

        if SRC and SVCT:
            msg_seg = {'class': 'bg-gradient-success', 'icon': 'check', 'message': SRC.id, 'data': SRC}
        else:
            msg_seg = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe seguros', 'data': SRC}

        if SOAT and CITV and SRC and SVCT:
            disable = ""
        else:
            disable = "disabled"

        forms = {'SOAT_F': form_soat, 'CITV_F': form_citv, 'SRC_F': form_src, 'SVCT_F': form_svct}
        context =   {
                        'segment': 'validate',
                        'sidebars': sidebar,
                        'title': title,
                        'page':'Validaciones',
                        'unit': vehicle,
                        'soat' : msg_soat,
                        'citv' : msg_citv,
                        'segc' : msg_seg,
                        'forms' : forms,
                        'disable' : disable,
                        'pk' : pk
                    }
        html_template = loader.get_template('validations/validate.html')
        return HttpResponse(html_template.render(context, request))



# Create your views here.
class SelectView(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones'}
        html_template = loader.get_template('validations/select.html')
        return HttpResponse(html_template.render(context, request))



# Create your views here.
class ProcedureRegister(HttpResponse):
    @login_required(login_url='/login/')
    def index(request, pk):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        unit = vehicles.objects.get(plate = pk)

        ROUTE_F = RoutesForm()
        PROCEDURE_F = ProcedureForm()
        SUBSTITUTION_F = SubstitutionForm()
        forms = {'form_r': ROUTE_F, 'form_p' : PROCEDURE_F, 'form_s' : SUBSTITUTION_F}

        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones', 'unit': unit, 'forms': forms}
        html_template = loader.get_template('procedure/create.html')
        return HttpResponse(html_template.render(context, request))

class ProcedureCreate(CreateAPIView):
    serializer_class = RouteSerializer

class ContractCreate(CreateAPIView):
    serializer_class = BindingContractsSerializer

class authorizaitonCreate(CreateAPIView):
    serializer_class = AuthorizationDocumentSerializer

class ValidateCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = procedure
    form_class = ProcedureForm
    success_message = 'Doc successfully created!'
    error_message = 'Error saving the Doc, check fields below.'
    template_name  = 'procedure/create.html'
    def get_success_url(self):
        return reverse('validate.index')

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

class YearAntiquity(ListAPIView):
    serializer_class = ValidationToolsSerializer

    def get_queryset(self):
        return validation_tools.objects.filter(status_years = True)

class ProcedureView(HttpResponse):
    @login_required(login_url='/login/')
    def index(request, pk):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        procedures = procedure.objects.get(id = pk)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Expediente ', 'procedure' : procedures}
        html_template = loader.get_template('procedure/view.html')
        return HttpResponse(html_template.render(context, request))