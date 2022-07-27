from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
import datetime
from datetime import datetime, date, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from django.contrib import messages
from django.views.generic import CreateView, FormView, TemplateView, UpdateView
from django.urls import reverse, reverse_lazy
import datetime

from apps.vehicles.models import vehicles
from apps.certify.models import soat, citv, src, svct
from apps.validations.models import authorization_documents, binding_contracts, routes, procedure, validation_tools

from apps.certify.forms import SOATForm, CITVForm, SRCForm, SVCTForm
from apps.validations.forms import RoutesForm, ProcedureForm, SubstitutionForm, binding_contractsForm, autauthorization_documents_form

from .serializers import RouteSerializer, BindingContractsSerializer, AuthorizationDocumentSerializer, ValidationToolsSerializer, ProcedureSerializer, substitutionSerializer
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
        id_v = pk.split('-', 1)[0]
        id_c = pk.split('-', 1)[1]
        print(id)
        msg_soat = dict
        now = datetime.datetime.now()
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)

        vehicle = vehicles.objects.filter(plate = id_v, status = True).first()

        SOAT = soat.objects.filter(vehicles=id_v, status=True).first()
        CITV = citv.objects.filter(vehicle=id_v, status=True).first()
        SRC = src.objects.filter(vehicles=id_v, status=True).first()
        SVCT = svct.objects.filter(vehicles=id_v, status=True).first()
        CONT = binding_contracts.objects.filter(id=id_c).first()
        try:
            ct = procedure.objects.all().get(license_plate = id_v)
        except procedure.DoesNotExist:
            ct = None

        PROC = ct


        form_soat = SOATForm()
        form_citv = CITVForm()
        form_src = SRCForm()
        form_svct = SVCTForm()
        form_cont = binding_contractsForm()

        if SOAT:
            msg_soat = {'class': 'bg-gradient-success', 'icon': 'check', 'message': SOAT.policy, 'data': SOAT}
        else:
            msg_soat = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe SOAT', 'data': SOAT}

        if CITV:
            msg_citv = {'class': 'bg-gradient-success', 'icon': 'check', 'message': CITV.id, 'data': CITV}
        else:
            msg_citv = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe CITV', 'data': CITV}

        if SRC:
            msg_src = {'class': 'bg-gradient-success', 'icon': 'check', 'message': SRC.id, 'data': SRC}
        else:
            msg_src = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe seguros', 'data': SRC}

        if SVCT:
            msg_svct = {'class': 'bg-gradient-success', 'icon': 'check', 'message': SVCT.id, 'data': SVCT}
        else:
            msg_svct = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe seguros', 'data': SVCT}

        if CONT:
            msg_cont = {'class': 'bg-gradient-success', 'icon': 'check', 'message': CONT.code, 'data': CONT}
            id_cont = CONT.id
        else:
            msg_cont = {'class': 'bg-gradient-danger', 'icon': 'error', 'message': 'No existe seguros', 'data': SVCT}
            id_cont = '0'

        if SOAT and CITV and SRC and SVCT:
            disable = ""
        else:
            disable = "disabled"

        forms = {'SOAT_F': form_soat, 'CITV_F': form_citv, 'SRC_F': form_src, 'SVCT_F': form_svct, 'CONT_F': form_cont}
        context =   {
                        'segment': 'validate',
                        'sidebars': sidebar,
                        'title': title,
                        'page':'Validaciones',
                        'unit': vehicle,
                        'soat' : msg_soat,
                        'procedure': PROC,
                        'citv' : msg_citv,
                        'src' : msg_src,
                        'svct' : msg_svct,
                        'cont' : msg_cont,
                        'forms' : forms,
                        'disable' : disable,
                        'pk' : pk,
                        'contract' : id_cont
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
        id_v = pk.split('-', 1)[0]
        id_c = pk.split('-', 1)[1]
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=7)
        unit = vehicles.objects.get(plate = id_v)

        ROUTE_F = RoutesForm()
        PROCEDURE_F = ProcedureForm()
        SUBSTITUTION_F = SubstitutionForm()
        forms = {'form_r': ROUTE_F, 'form_p' : PROCEDURE_F, 'form_s' : SUBSTITUTION_F}

        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Validaciones', 'unit': unit, 'forms': forms}
        html_template = loader.get_template('procedure/create.html')
        return HttpResponse(html_template.render(context, request))

class ValidationForm(LoginRequiredMixin, FormView):
    login_url = '/login/'
    form_class = ProcedureForm
    template_name = 'validations/create.html'
    success_url = reverse_lazy('validate.index')

    def get_code_type(self, id):
        pk = self.kwargs['pk']
        return pk.split('-',1)[id]

    def get_soat(self):
        try:
            ct = soat.objects.all().filter(vehicles = self.get_code_type(0)).order_by('create_at')
            if ct.count() > 1:
                s = ct
            else:
                s = soat.objects.all().get(vehicles = self.get_code_type(0))

        except soat.DoesNotExist:
            s = None
        return s

    def get_citv(self):
        try:
            ct = citv.objects.all().filter(vehicle = self.get_code_type(0)).order_by('created_at')
            if ct.count() > 1:
                c = ct
            else:
                c = citv.objects.all().get(vehicle = self.get_code_type(0))

        except citv.DoesNotExist:
            c = None
        return c

    def get_src(self):
        try:
            ct = src.objects.all().filter(vehicles = self.get_code_type(0)).order_by('create_at')
            if ct.count() > 1:
                c = ct
            else:
                c = src.objects.all().get(vehicles = self.get_code_type(0))
        except src.DoesNotExist:
            c = None
        return c
    def get_svct(self):
        try:
            ct = svct.objects.all().filter(vehicles = self.get_code_type(0)).order_by('create_at')
            if ct.count() > 1:
                c = ct
            else:
                c = svct.objects.all().get(vehicles = self.get_code_type(0))
        except svct.DoesNotExist:
            c = None
        return c
    def get_contract(self):
        try:
            c = binding_contracts.objects.all().get(id = self.get_code_type(1))
        except binding_contracts.DoesNotExist:
            c = None
        return c

    def get_enable_status(self):
        try:
            if self.get_soat():
                if self.get_citv():
                    if self.get_src():
                        if self.get_svct():
                            if self.get_contract():
                                hability = 'ACEPTADO'
                                message_h = 'Registros previos correctos'
                                background = 'transparent text-dark'
                            else:
                                hability = 'PENDIENTE'
                                message_h = 'Falta Contratos, SVCT, SRC, CITV y SOAT'
                                background = 'warning'
                        else:
                            hability = 'PENDIENTE'
                            message_h = 'Falta SVCT, SRC, CITV, SOAT'
                            background = 'warning'
                    else:
                        hability = 'PENDIENTE'
                        message_h = 'Falta SRC, CITV, SOAT'
                        background = 'warning'
                else:
                    hability = 'PENDIENTE'
                    message_h = 'Falta CITV, SOAT'
                    background = 'warning'
            else:
                hability = 'PENDIENTE'
                message_h = 'Falta SOAT'
                background = 'warning'
            return {'enable' : hability, 'background': background, 'msg' : message_h}
        except:
            pass

    def get_context_data(self, **kwargs):
        print(self.get_citv())
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['segment'] = 'validate'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=7)
        context['page'] = 'Crear una validacion'
        context['vehicle'] = vehicles.objects.get(plate = pk.split('-',1)[0])
        context['authorization_form'] = autauthorization_documents_form()
        context['substitution_form'] = SubstitutionForm()
        context['soat'] = self.get_soat()
        context['citv'] = self.get_citv()
        context['src'] = self.get_src()
        context['svct'] = self.get_svct()
        context['contract'] = self.get_contract()
        context['total'] = procedure.objects.all()
        context['enable'] = self.get_enable_status()
        return context

class ProcedureCreate(CreateAPIView):
    serializer_class = RouteSerializer

class procedureAPIList(ListAPIView):
    queryset = procedure.objects.all()
    serializer_class = ProcedureSerializer
    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return procedure.objects.filter(license_plate = kword)

class ContractAPICreate(CreateAPIView):
    serializer_class = BindingContractsSerializer

class ContractCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = binding_contracts
    form_class = binding_contractsForm
    #success_url = reverse_lazy('validate.val')
    def get_vehiclie_id(self):
        return self.kwargs['plate']

    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.get_vehiclie_id() + '-' + str(self.object.id),
        })

class authorizaitonCreate(CreateAPIView):
    serializer_class = AuthorizationDocumentSerializer

class substitutionCreate(CreateAPIView):
    serializer_class = substitutionSerializer

class authorizationCreate(CreateView):
    model = authorization_documents
    form_class = autauthorization_documents_form
    success_url = reverse_lazy('validations/')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                if self.is_valid():
                    data = self.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

class ValidateCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = procedure
    form_class = ProcedureForm

    def post(self, request,  *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'no ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

class ValidateUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = procedure
    form_class = ProcedureForm
    template_name = 'validations/update.html'
    success_url = reverse_lazy('/validations/')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,  *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'no ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'validate'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=7)
        context['page'] = 'Actualizar validacion'
        context['procedure'] = procedure.objects.get(id = self.kwargs['pk'])

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
        html_template = loader.get_template('validations/view.html')
        return HttpResponse(html_template.render(context, request))

class ProcedureViewList(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'validations/view.html'

    def get_list_procedure(self):
        try:
            code = procedure.objects.get(id = self.kwargs['pk'])
            ct = procedure.objects.all().filter(proceedings = code.proceedings)
            if ct.count() > 1:
                c = ct
            else:
                c = procedure.objects.all().get(proceedings = code.proceedings)
        except procedure.DoesNotExist:
            c = None
        return c

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['segment'] = 'validate'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=7)
        context['page'] = 'Crear una validacion'
        context['procedure'] = procedure.objects.get(id = self.kwargs['pk'])
        context['list'] = self.get_list_procedure()
        return context