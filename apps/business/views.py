import re
from rest_framework.generics import CreateAPIView, ListAPIView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from apps.includes.sidebar.models import Sidebar
from apps.business.forms import BusinessForm
from apps.business.models import business


from .serializers import BusinessSerializers
# Create your views here.


class IndexView(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=4)
        bs = business.objects.all()

        context = {'segment': 'business', 'sidebars': sidebar, 'title': title, 'page':'Empresas', 'business': bs}
        html_template = loader.get_template('business/index.html')
        return HttpResponse(html_template.render(context, request))

class BusinessCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = business
    template_name = 'business/create.html'
    form_class = BusinessForm
    success_url = reverse_lazy('business.index')
    success_message = 'Doc successfully created!'
    error_message = "Error saving the Doc, check fields below."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(BusinessCreate, self).get_context_data(**kwargs)
        context['segment'] = 'business'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=4)
        context['page'] = 'Crear empresa'

        return context

class BusinessUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = business
    template_name = 'business/update.html'
    form_class = BusinessForm
    success_url = reverse_lazy('business.index')

    def save(self,*args, **kwargs):
        self.small_name = self.small_name.upper()
        return super(business, self).save(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BusinessUpdate, self).get_context_data(**kwargs)
        context['segment'] = 'business'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=4)
        context['page'] = 'Actualizar empresar'
        context['pk'] = self.kwargs['pk']
        return context

class BusinessView(HttpResponse):
    @login_required(login_url='/login/')
    def index(request, pk):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=4)
        bs = business.objects.get(ruc=pk)

        context = {'segment': 'business', 'sidebars': sidebar, 'title': title, 'page':'Empresas', 'business': bs}
        html_template = loader.get_template('business/view.html')
        return HttpResponse(html_template.render(context, request))

class BusinessDeleteSoft(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = business

    def post(self, request, pk, *args, **kwargs):
        data = {}
        try:
            object = business.objects.get(ruc = pk)
            object.delete_at = datetime.datetime.now()
            object.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

class BusinessIndex(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = business
    template_name  = 'business/index.html'
    paginate_by = 50

    def get_queryset(self):
        return business.objects.order_by('ruc').filter(delete_at__isnull=True)

    def get_context_data(self, **kwargs):
        context = super(BusinessIndex, self).get_context_data(**kwargs)
        context['segment'] = 'Business'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=4)
        context['page'] = 'Listar empresas'
        return context

""" services start here """
class businessAPICreate(CreateAPIView):
    serializer_class = BusinessSerializers

class businessAPIList(ListAPIView):
    serializer_class = BusinessSerializers

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return business.objects.filter(name__icontains = kword)