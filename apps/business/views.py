import re
from rest_framework.generics import CreateAPIView, ListAPIView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.includes.sidebar.models import Sidebar
from apps.business.forms import BusinessForm
from apps.business.models import business


from .serializers import BusinessSerializers
# Create your views here.

@login_required(login_url='/login/')
class ListView(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=4)
        bs = business.objects.all()

        context = {'segment': 'business', 'sidebars': sidebar, 'title': title, 'page':'Empresas', 'business': bs}
        html_template = loader.get_template('business/index.html')
        return HttpResponse(html_template.render(context, request))

class BusinessCreate(CreateView):
    model = business
    template_name = 'business/create.html'
    form_class = BusinessForm
    success_url = reverse_lazy('business.index')

    def get_context_data(self, **kwargs):
        context = super(BusinessCreate, self).get_context_data(**kwargs)
        context['segment'] = 'business'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=4)
        context['page'] = 'Actualizar vehiculo'
        return context

""" services start here """
class businessAPICreate(CreateAPIView):
    serializer_class = BusinessSerializers

class businessAPIList(ListAPIView):
    serializer_class = BusinessSerializers

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return business.objects.filter(name__icontains = kword)