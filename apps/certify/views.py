from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.template import loader

from apps.includes.sidebar.models import Sidebar
from apps.certify.models import citv, soat, src, svct
from apps.certify.forms import CITVForm, SOATForm, SRCForm, SVCTForm
from .serializers import SOATSerializer, CITVSerializer, SRCSerializer, SVCTSerializer
from apps.certify import serializers
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

class ValidateLegal(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=6)
        print(request);
        context = {'segment': 'certify', 'sidebars': sidebar, 'title': title, 'page':'Certificados'}
        html_template = loader.get_template('certify/select.html')
        return HttpResponse(html_template.render(context, request))

class CreateSOAT(HttpResponse):
    def index(request):
        if request.method == "POST":
            form = SOATForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                plate = request.POST['vehicles']
            else:
                messages.error(request, form)
        else:
            messages.error(request, form)
        return redirect('validate.val', pk=plate)

""" services start here """
class API_ValidateLegalSOAT(ListAPIView):
    serializer_class = SOATSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicles']

    def get_queryset(self):
        queryset = soat.objects.all().select_related('vehicles')
        return queryset.filter(status = True)

class API_ValidateLegalCITV(ListAPIView):
    serializer_class = CITVSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicle']
    def get_queryset(self):
        queryset = citv.objects.all().select_related('vehicle')
        return queryset.filter(status = True)

class API_ValidateLegalSRC(ListAPIView):
    serializer_class = SRCSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicles']
    def get_queryset(self):
        queryset = src.objects.all().select_related('vehicles')
        return queryset.filter(status = True)

class createAPI_SOAT(CreateView):
    model = soat
    form_class = SOATForm
    #success_url = reverse_lazy('validate.val')
    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicles.pk,
        })

class createAPI_CITV(CreateView):
    model = citv
    form_class = CITVForm
    #success_url = reverse_lazy('validate.val')
    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicle.pk
        })

class createAPI_SRC(CreateView):
    model = src
    form_class = SRCForm

    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicles.pk,
        })

class createAPI_SVCT(CreateView):
    model = svct
    form_class = SVCTForm

    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicles.pk
        })