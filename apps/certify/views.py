from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.template import loader
from apps.includes.sidebar.models import Sidebar
from apps.certify.models import soat
from apps.certify.forms import SOATForm
from .serializers import SOATSerializer, CITVSerializer
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
            else:
                messages.error(request, form)
        else:
            messages.error(request, form)
        return redirect('validate.val')

""" services start here """
class API_ValidateLegal(ListAPIView):
    serializer_class = SOATSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicles']

    def get_queryset(self):
        queryset = soat.objects.all().select_related('vehicles')
        return queryset.filter(status = True)

class createAPI_SOAT(CreateAPIView):
    serializer_class = SOATSerializer

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('validate.val', plate=self.vehicles)

class createAPI_CITV(CreateAPIView):
    serializer_class = CITVSerializer

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('validate.val', plate=self.vehicle)