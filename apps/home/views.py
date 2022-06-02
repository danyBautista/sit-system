# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

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

@login_required(login_url="/login/")
class DashboardHome(HttpResponse):
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
                    'business' : bu
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
