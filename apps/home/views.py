# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from wsgiref import validate
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, GenericAPIView
from crum import get_current_request
from dataclasses import dataclass
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, JsonResponse

from apps.includes.sidebar.models import Sidebar
from apps.validations.models import routes
from apps.accreditation.models import accreditation, accreditation_type
from apps.vehicles.models import vehicles
from apps.people.models import people
from apps.business.models import business
from apps.validations.models import procedure
from apps.home.models import Consulting
from apps.home.forms import ConsultingForm
from apps.home.mixins import IsSuperuserMixin

from apps.vehicles.serializers import VehiclesSerializer
from .serializers import ConsultingSerializer
from core.user.models import User

class DashboardView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = 'home.view_category'
    login_url = '/login/'
    template_name = 'home/index.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **Kwargs):
        request.user.get_group_session()
        return super().get(request, *args, **Kwargs)

    def get_graph_accreditation_concesion(self):
            data = []
            concession = ['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11']
            add = []
            try:
                types = accreditation_type.objects.all().filter(status = True)

                for n in types:
                    series = n.name
                    c2 = accreditation.objects.all().filter(route__concession = 'C2', type = n.id).count()
                    c3 = accreditation.objects.all().filter(route__concession = 'C3', type = n.id).count()
                    c4 = accreditation.objects.all().filter(route__concession = 'C4', type = n.id).count()
                    c5 = accreditation.objects.all().filter(route__concession = 'C5', type = n.id).count()
                    c6 = accreditation.objects.all().filter(route__concession = 'C6', type = n.id).count()
                    c7 = accreditation.objects.all().filter(route__concession = 'C7', type = n.id).count()
                    c8 = accreditation.objects.all().filter(route__concession = 'C8', type = n.id).count()
                    c9 = accreditation.objects.all().filter(route__concession = 'C9', type = n.id).count()
                    c10 = accreditation.objects.all().filter(route__concession = 'C10', type = n.id).count()
                    c11 = accreditation.objects.all().filter(route__concession = 'C11', type = n.id).count()

                    content = {'name' : series, 'data': [c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]}
                    data.append(content)
            except:
                pass

            return data

    def get_cards_data(self):
        data = []
        vehicle = vehicles.objects.all()
        data.append(vehicle)
        return data

    def get_accredite_percent(self):
        data = []
        accredite_type = accreditation_type.objects.all().filter(status = True)
        for item in accredite_type:
            content = {
                'name': item.name,
                'icon' : item.icon,
                'color' : item.color,
                'count': accreditation.objects.all().filter(type = item.id).count,
                'link' : '/reports/accreditation/'
            }
            data.append(content)
        acredite = accreditation.objects.all().filter(type = 1).count
        total_ac = accreditation.objects.all().count
        #percent = acredite * 100 / total_ac
        return (data)

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['segment'] = 'index'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=1)
        context['page'] = 'Crear Acreditacion'
        context['action'] = 'add'
        context['vehicle'] = vehicles.objects.all()
        context['people'] = people.objects.all()
        context['business'] = business.objects.all()
        context['validation'] = procedure.objects.all()
        context['accreditation'] = self.get_accredite_percent()
        context['graph_accreditation_with_consesion'] = self.get_graph_accreditation_concesion()
        return context

class DashboardHome(HttpResponse):
    @login_required(login_url="/login/")

    def index(request):
        sidebar = Sidebar.objects.all()
        vh = vehicles.objects.all()
        pe = people.objects.all()
        bu = business.objects.all()

        consession = routes.objects.all().order_by('concession').distinct('concession').filter(concession__isnull = False)
        route = routes.objects.filter(concession='C2')
        type = accreditation_type.objects.all().filter(status = True)
        accred = accreditation.objects.all()
        pending = accreditation.objects.all().filter(status = 'PENDIENTE')
        retired = accreditation.objects.all().filter(status = 'RETIRADO')
        DataChar = {
            'C2_A' : accreditation.objects.all().filter(route__concession = 'C2', status='ACREDITADO').count(),
            'C3_A' : accreditation.objects.all().filter(route__concession = 'C3', status='ACREDITADO').count(),
            'C4_A' : accreditation.objects.all().filter(route__concession = 'C4', status='ACREDITADO').count(),
            'C5_A' : accreditation.objects.all().filter(route__concession = 'C5', status='ACREDITADO').count(),
            'C6_A' : accreditation.objects.all().filter(route__concession = 'C6', status='ACREDITADO').count(),
            'C7_A' : accreditation.objects.all().filter(route__concession = 'C7', status='ACREDITADO').count(),
            'C8_A' : accreditation.objects.all().filter(route__concession = 'C8', status='ACREDITADO').count(),
            'C9_A' : accreditation.objects.all().filter(route__concession = 'C9', status='ACREDITADO').count(),
            'C10_A' : accreditation.objects.all().filter(route__concession = 'C10', status='ACREDITADO').count(),
            'C11_A' : accreditation.objects.all().filter(route__concession = 'C11', status='ACREDITADO').count(),
            'C2_P' : accreditation.objects.all().filter(route__concession = 'C2', status='PENDIENTE').count(),
            'C3_P' : accreditation.objects.all().filter(route__concession = 'C3', status='PENDIENTE').count(),
            'C4_P' : accreditation.objects.all().filter(route__concession = 'C4', status='PENDIENTE').count(),
            'C5_P' : accreditation.objects.all().filter(route__concession = 'C5', status='PENDIENTE').count(),
            'C6_P' : accreditation.objects.all().filter(route__concession = 'C6', status='PENDIENTE').count(),
            'C7_P' : accreditation.objects.all().filter(route__concession = 'C7', status='PENDIENTE').count(),
            'C8_P' : accreditation.objects.all().filter(route__concession = 'C8', status='PENDIENTE').count(),
            'C9_P' : accreditation.objects.all().filter(route__concession = 'C9', status='PENDIENTE').count(),
            'C10_P' : accreditation.objects.all().filter(route__concession = 'C10', status='PENDIENTE').count(),
            'C11_P' : accreditation.objects.all().filter(route__concession = 'C11', status='PENDIENTE').count(),
            'C2_R' : accreditation.objects.all().filter(route__concession = 'C2', status='RETIRADO').count(),
            'C3_R' : accreditation.objects.all().filter(route__concession = 'C3', status='RETIRADO').count(),
            'C4_R' : accreditation.objects.all().filter(route__concession = 'C4', status='RETIRADO').count(),
            'C5_R' : accreditation.objects.all().filter(route__concession = 'C5', status='RETIRADO').count(),
            'C6_R' : accreditation.objects.all().filter(route__concession = 'C6', status='RETIRADO').count(),
            'C7_R' : accreditation.objects.all().filter(route__concession = 'C7', status='RETIRADO').count(),
            'C8_R' : accreditation.objects.all().filter(route__concession = 'C8', status='RETIRADO').count(),
            'C9_R' : accreditation.objects.all().filter(route__concession = 'C9', status='RETIRADO').count(),
            'C10_R' : accreditation.objects.all().filter(route__concession = 'C10', status='RETIRADO').count(),
            'C11_R' : accreditation.objects.all().filter(route__concession = 'C11', status='RETIRADO').count()
        }
        context = {
                    'segment': 'index',
                    'sidebars': sidebar,
                    'pk' : 1,
                    'graph_accreditation_with_consesion' : self,
                    'concession' : 'C2',
                    'concessions' : consession,
                    'accreditation': accred,
                    'pending' : pending,
                    'retired' : retired,
                    'vehicles' : vh,
                    'people' : pe,
                    'business' : bu,
                    'data' : DataChar,
                    'type' : type
                }

        html_template = loader.get_template('home/index.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

class TemplatePage(TemplateView):
    template_name = 'home/web.html'

class ConsultingAPIView(ListAPIView):
    serializer_class = VehiclesSerializer

    def get_queryset(self):
        pk = self.kwargs['key']
        return vehicles.objects.filter(plate=pk)

class ConsultingAPICreate(CreateAPIView):
        serializer_class = ConsultingSerializer

class ConsultingView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'home/query.html'
    def get_percent_accreditation(self):
        percent = 0
        try:
            accre = accreditation.objects.get(plate = self.kwargs['key'])
            if(accre.legal_requirements == 'CUMPLE'):
                percent = percent + 20
            if(accre.technical_requirements == 'CUMPLE'):
                percent = percent + 20
            if(accre.technical_requirements == 'CUMPLE'):
                percent = percent + 20
            if(accre.insurance == 'CUMPLE'):
                percent = percent + 20
            if(accre.accreditation_card == True):
                percent = percent + 20
            return percent
        except accreditation.DoesNotExist:
            accre = None
        return accre

    def get_percent_validation(self):
        percent = 0
        #vali = procedure.objects.get(license_plate = self.kwargs['key']).first()

        return percent

    def get_validation(self):
        try:
            content = procedure.objects.get(license_plate = self.kwargs['key'])
        except procedure.DoesNotExist:
            content = None
        return content
    def get_accreditation(self):
        try:
            accr = accreditation.objects.get(plate = self.kwargs['key'])
        except accreditation.DoesNotExist:
            accr = None
        return accr

    def get_context_data(self, **kwargs):
        context = super(ConsultingView, self).get_context_data(**kwargs)
        context['segment'] = 'index'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=1)
        context['vehicle'] = vehicles.objects.get(plate = self.kwargs['key'])
        context['accreditation'] = self.get_accreditation()
        context['percent_accreditation'] = self.get_percent_accreditation()
        context['validation'] = self.get_validation()
        context['percent_validaiton'] = self.get_percent_validation()
        context['page'] = 'Crear Acreditacion'
        return context