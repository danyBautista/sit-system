# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django import template
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import datetime
from django.template import loader
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.people.models import people
from apps.includes.sidebar.models import Sidebar
from apps.people.forms import PeopleForm
from .serializers import PeopleSerializer
# Create your views here.

class PeopleIndex(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = people
    template_name  = 'people/index.html'
    paginate_by = 50

    def get_queryset(self):
        return people.objects.order_by('dni').filter(delete_at__isnull=True)

    def get_context_data(self, **kwargs):
        context = super(PeopleIndex, self).get_context_data(**kwargs)
        context['segment'] = 'people'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=3)
        context['page'] = 'Crear Usuario'
        return context

class PeopleCreate(LoginRequiredMixin, CreateView):
    model = people
    template_name  = 'people/create.html'
    form_class = PeopleForm
    success_url = reverse_lazy('people.index')

    def get_context_data(self, **kwargs):
        context = super(PeopleCreate, self).get_context_data(**kwargs)
        context['segment'] = 'people'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=3)
        context['page'] = 'Crear Propietario'
        return context

class PeopleUpdate(LoginRequiredMixin, UpdateView):
    model = people
    template_name  = 'people/update.html'
    form_class = PeopleForm
    success_url = reverse_lazy('people.index')

    def get_context_data(self, **kwargs):
        context = super(PeopleUpdate, self).get_context_data(**kwargs)
        context['segment'] = 'people'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=3)
        context['page'] = 'Actualizar Propietario'
        context['pk'] = self.kwargs['pk']
        return context

def view(request, key_id):
    user = people.objects.get(dni=key_id)
    sidebar = Sidebar.objects.all()
    context = {'segment': 'people', 'sidebars': sidebar, 'people': user, 'title': 'Usuarios', 'page':'usuario/perfil'}
    html_template = loader.get_template('people/profile.html')
    return HttpResponse(html_template.render(context, request))

""" services start here """

class PeopleListAPIView(ListAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return people.objects.filter(name__icontains = kword)

class PeopleSearchDNI(ListAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self):
        dni = self.request.query_params.get('kword', '')
        return people.objects.filter(dni__icontains = dni)

class SelectAPIView(ListAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return people.objects.filter(dni=pk)

class PeopleUpdateAPIView(UpdateAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(status = True).filter(dni = pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            PeopleSerializer = self.serializer_class(self.get_queryset(pk))
            return Response(PeopleSerializer.data)
        return Response({'error':'No existe usuario con estos datos!'})

    def put(self, request, pk=None):

        if self.get_queryset(pk):
            PeopleSerializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if PeopleSerializer.is_valid():
                PeopleSerializer.save()
                return Response(PeopleSerializer.data)
            return Response(PeopleSerializer.errors)

class PeopleCreateAPI(CreateAPIView):
    serializer_class = PeopleSerializer

class PeopleDeleteSoft(LoginRequiredMixin, DeleteView):
    model = people

    def post(self, request, pk, *args, **kwargs):
        data = {}
        try:
            object = people.objects.get(dni = pk)
            object.delete_at = datetime.datetime.now()
            object.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)