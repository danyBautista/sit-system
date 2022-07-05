# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""
from apps import administration
from core.user.forms import UserForm
from rest_framework.generics import CreateAPIView, ListAPIView

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DeleteView, View, FormView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

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
    form_class = UserForm
    success_url = reverse_lazy('administration/user/')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        context['segment'] = 'administration'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=2)
        context['page'] = 'Crear usuario de sistema'
        return context

class UserUpdate( UpdateView):
    #login_url = '/login/'LoginRequiredMixin,
    model = User
    template_name = 'administration/users/update.html'
    form_class = UserForm
    success_url = reverse_lazy('administration/user')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        context['segment'] = 'administration'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=2)
        context['page'] = 'Crear usuario de sistema'
        context['code'] = self.kwargs['pk']
        return context

class UserApiList(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return User.objects.filter(first_name__icontains = kword)

class UserChangeGroup(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            request.session['group'] = Group.objects.get(pk = self.kwargs['pk'])
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('home'))

class UserPasswordChangeView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    form_class = PasswordChangeForm
    template_name = 'administration/users/password-change.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'eddit':
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(UserPasswordChangeView, self).get_context_data(**kwargs)
        context['segment'] = 'administration'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=2)
        context['page'] = 'Edicion de la contraseña'
        return context