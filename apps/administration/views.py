# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""
from rest_framework.generics import CreateAPIView, ListAPIView

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.includes.sidebar.models import Sidebar
from core.user.models import User
from .serializers import UserSerializer

# Create your views here.
class AdminIndex(HttpResponse):
    @login_required(login_url="/login/")
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=2)
        user = User.objects.all()
        context = {'segment': 'administration', 'sidebars': sidebar, 'title': title, 'page':'Reportes', 'user' : user}
        html_template = loader.get_template('administration/index.html')
        return HttpResponse(html_template.render(context, request))

class UserIndex(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = User
    template_name = 'administration/users/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserIndex, self).get_context_data(**kwargs)
        context['segment'] = 'administration'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=2)
        context['page'] = 'Listar empresas'
        return context

class UserCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = User
    template_name = 'administration/users/create.html'

    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        context['segment'] = 'administration'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=2)
        context['page'] = 'Listar empresas'
        return context

class UserApiList(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return User.objects.filter(first_name__icontains = kword)