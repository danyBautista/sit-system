from apps.validations.models import procedure
from rest_framework.generics import CreateAPIView, ListAPIView
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core import serializers

from apps.accreditation.forms import accreditationsForm, typeForm
from apps.accreditation.models import accreditation, accreditation_type
from apps.accreditation.mixins import ValidatePermissionRequiredMixin
from apps.includes.sidebar.models import Sidebar
from apps.vehicles.models import vehicles
from .serializers import serialiazerType
# Create your views here.

class accreditationIndex(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    login_url = '/login/'
    model = accreditation
    template_name  = 'accreditation/index.html'
    paginate_by = 50

    def get_queryset(self):
        return accreditation.objects.order_by('plate').filter(delete_at__isnull=True)

    def get_context_data(self, **kwargs):
        context = super(accreditationIndex, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['page'] = 'Crear Propietario'
        return context

class accreditationCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = accreditation
    template_name = 'accreditation/create.html'
    form_class = accreditationsForm
    success_url = reverse_lazy('accreditation.index')
    success_message = 'Doc successfully created!'
    error_message = "Error saving the Doc, check fields below."

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

class accreditationView(HttpResponse):
    @login_required(login_url="/login/")
    def index(request, pk):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=10)
        ac = accreditation.objects.get(id=pk)

        context = {'segment': 'business', 'sidebars': sidebar, 'title': title, 'page':'Empresas', 'accreditation': ac}
        html_template = loader.get_template('accreditation/view.html')
        return HttpResponse(html_template.render(context, request))

class accreditationUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = accreditation
    template_name = 'accreditation/update.html'
    form_class = accreditationsForm
    success_url = reverse_lazy('accreditation.index')

    def get_context_data(self, **kwargs):
        context = super(accreditationUpdate, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['page'] = 'Actualizar acreditacion'
        context['pk'] = self.kwargs['pk']
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class TypeCreate(CreateView):
    model = accreditation_type
    form_class = typeForm
    success_url = reverse_lazy('accreditation.create')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    instance = form.save()
                    data['success'] = serializers.serialize('json', [ instance, ])
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'no ha ingresado a ninguna opcion'
            #data = accreditation_type.post(id=request.POST['id']).toJson().toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

class accreditationSearch(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'accreditation/search.html'

    def get_context_data(self, **kwargs):
        context = super(accreditationSearch, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['page'] = 'Actualizar acreditacion'
        return context

class accreditationForm(LoginRequiredMixin, FormView):
    login_url = '/login/'
    template_name = 'accreditation/create.html'
    form_class = accreditationsForm

    def get_procedure(self):
        try:
            pros = procedure.objects.all().get(id = self.kwargs['pk'])
        except accreditation.DoesNotExist:
            pros = None
        return pros

    def get_mechanical_inspection(self):
        try:
            proc = procedure.objects.all().get(id = self.kwargs['pk'])
            if proc:
                if proc.soat_status == 'VIGENTE':
                    status = 'CUMPLE'
                else:
                    if proc.soat_status == 'NO VIGENTE':
                        status = 'NO CUMPLE'
                    else:
                        status = 'PENDIENTE'
        except procedure.DoesNotExist:
            proc = None
        return status

    def get_mechanical_inspection(self):
        proc = procedure.objects.all().get(id = self.kwargs['pk'])
        if proc:
            if proc.citv_status == 'VIGENTE':
                status = 'CUMPLE'
            else:
                if proc.citv_status == 'NO VIGENTE':
                    status = 'NO CUMPLE'
                else:
                    status = 'PENDIENTE'
        return status

    def get_technical_requirements(self):
        try:
            proc = procedure.objects.all().get(id = self.kwargs['pk'])
            if proc:
                if proc.src_status == 'VIGENTE' and proc.citv_status == 'VIGENTE' and proc.bonding_contract and proc.check_sistran == True:
                    status = 'CUMPLE'
                else:
                    if proc.src_status == 'NO VIGENTE' or proc.svct_status == 'NO VIGENTE' or proc.bonding_contract or proc.check_sistran == False:
                        status = 'NO CUMPLE'
                    else:
                        status = 'OBSERVADO'
        except procedure.DoesNotExist:
            proc = None
        return status

    def get_context_data(self, **kwargs):
        context = super(accreditationForm, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['procedure'] = self.get_procedure()
        context['insurance'] = self.get_mechanical_inspection()
        context['mechanical_inspection'] = self.get_mechanical_inspection()
        context['technical_requirements'] = self.get_technical_requirements()
        context['page'] = 'Actualizar acreditacion'
        return context