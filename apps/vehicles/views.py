from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib import messages

from apps.includes.sidebar.models import Sidebar
from apps.vehicles.models import vehicles, types
from apps.vehicles.forms import VehicleForm, TypeVehicleForm
from .serializers import (
    VehiclesSerializer,
    TypesVehiclesSerializer
)

# Create your views here.

@login_required(login_url='/login/')
# Create your views here.
class VehiclesViews(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=5)
        units = vehicles.objects.all()
        context = {'segment': 'vehicles', 'sidebars': sidebar, 'title': title, 'page':'Vehiculos', 'vehicles': units}
        html_template = loader.get_template('vehicles/index.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url='/login/')
class VehiclesCreate(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=5)
        if request.method == "POST":
            form = VehicleForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, form)
            return redirect('vehicles.index')
        else:
            form = VehicleForm()

        context = {'segment': 'vehicles', 'sidebars': sidebar, 'title': title, 'page':'Vehiculos', 'form' : form}
        html_template = loader.get_template('vehicles/create.html')
        return HttpResponse(html_template.render(context, request))

""" services start here """
class VehiclesListAPIView(ListAPIView):
    serializer_class = VehiclesSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return vehicles.objects.filter(plate__icontains = kword)

class CreateTypeVehicle(CreateAPIView):
    serializer_class = TypesVehiclesSerializer

class TypeVehicleList(ListAPIView):
    serializer_class = TypesVehiclesSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return types.objects.filter(name__icontains = kword)