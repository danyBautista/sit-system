# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from dataclasses import dataclass
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from apps.includes.sidebar.models import Sidebar
from apps.validations.models import routes
from apps.accreditation.models import accreditation
from apps.vehicles.models import vehicles
from apps.people.models import people
from apps.business.models import business


class DashboardHome(HttpResponse):
    @login_required(login_url="/login/")
    def index(request):
        sidebar = Sidebar.objects.all()
        vh = vehicles.objects.all()
        pe = people.objects.all()
        bu = business.objects.all()

        consession = routes.objects.all().order_by('concession').distinct('concession').filter(concession__isnull = False)
        route = routes.objects.filter(concession='C2')
        approved = accreditation.objects.all().filter(status = 'ACREDITADO')
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
                    'concession' : 'C2',
                    'concessions' : consession,
                    'approved': approved,
                    'pending' : pending,
                    'retired' : retired,
                    'vehicles' : vh,
                    'people' : pe,
                    'business' : bu,
                    'data' : DataChar
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
