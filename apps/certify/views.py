from apps.validations.models import procedure
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy
from django.template import loader

from apps.includes.sidebar.models import Sidebar
from apps.certify.models import citv, soat, src, svct
from apps.certify.forms import CITVForm, SOATForm, SRCForm, SVCTForm
from .serializers import SOATSerializer, CITVSerializer, SRCSerializer, SVCTSerializer
from apps.certify import serializers
# Create your views here.



# Create your views here.
class CertifyView(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=6)
        _citv = citv.objects.all()
        _soat = soat.objects.all()
        _src = src.objects.all()
        _svct = svct.objects.all()
        context = {
                    'segment': 'certify', 
                    'sidebars': sidebar,
                    'title': title,
                    'page':'Certificados',
                    'CITV' : _citv,
                    'SOAT' : _soat,
                    'SRC' : _src,
                    'SVCT' : _svct
                }
        html_template = loader.get_template('certify/index.html')
        return HttpResponse(html_template.render(context, request))

class CertifyList(HttpResponse):
    @login_required(login_url='/login/')
    def index(request, type):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=6)
        if type == 'CITV':
            list = citv.objects.all()
        elif type == 'SOAT':
            list = soat.objects.all()
        elif type == 'SRC':
            list = src.objects.all()
        else:
            list = svct.objects.all()
        context = {
                    'segment': 'certify',
                    'sidebars': sidebar,
                    'title': title,
                    'page': type,
                    'list' : list
                }
        html_template = loader.get_template('certify/list.html')
        return HttpResponse(html_template.render(context, request))

class ValidateLegal(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=6)
        print(request);
        context = {'segment': 'certify', 'sidebars': sidebar, 'title': title, 'page':'Certificados'}
        html_template = loader.get_template('certify/select.html')
        return HttpResponse(html_template.render(context, request))

class CreateSOAT(HttpResponse):
    @login_required(login_url='/login/')
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

    def get_queryset(self):
        SOAT = soat.objects.all()
        return SOAT

    def get(self, request, *args, **kwargs):
        id = request.query_params['id']
        SOAT = soat.objects.get(id = id)
        serializers = SOATSerializer(SOAT)

        return Response(serializers.data)

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

class API_ValidateLegalSVCT(ListAPIView):
    serializer_class = SVCTSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicles']
    def get_queryset(self):
        queryset = svct.objects.all().select_related('vehicles')
        return queryset.filter(status = True)

class createAPI_SOAT(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = soat
    form_class = SOATForm
    #success_url = reverse_lazy('validate.val')
    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicles.pk + '-' + str(self.kwargs['key']),
        })

class createAPI_CITV(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = citv
    form_class = CITVForm
    #success_url = reverse_lazy('validate.val')
    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicle.pk + '-' + str(self.kwargs['key'])
        })

class createAPI_SRC(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = src
    form_class = SRCForm

    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicles.pk + '-' + str(self.kwargs['key']),
        })

class createAPI_SVCT(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = svct
    form_class = SVCTForm

    def get_success_url(self):
        return reverse('validate.val', kwargs={
            'pk': self.object.vehicles.pk + '-' + str(self.kwargs['key'])
        })

class CertifyQuery(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'None'
    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data['success'] = 'correcto' + self.kwargs['pk']
        except Exception as e:
            data['error'] = 'error ' + str(e)
        return super().get(request, *args, **kwargs)