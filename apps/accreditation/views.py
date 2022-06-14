from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from apps.accreditation.forms import accreditationsForm
from apps.accreditation.models import accreditation
from apps.includes.sidebar.models import Sidebar
from apps.vehicles.models import vehicles
# Create your views here.

class accreditationIndex(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = accreditation
    template_name  = 'accreditation/index.html'
    paginate_by = 50

    def get_queryset(self):
        return accreditation.objects.order_by('plate').filter(delete_at__isnull=True)

    def get_context_data(self, **kwargs):
        context = super(accreditationIndex, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['page'] = 'Crear Propietario'
        return context

class accreditationCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = accreditation
    template_name = 'accreditation/create.html'
    form_class = accreditationsForm
    success_url = reverse_lazy('accreditation.index')
    success_message = 'Doc successfully created!'
    error_message = "Error saving the Doc, check fields below."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(accreditationCreate, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['page'] = 'Crear Acreditacion'

        return context

class accreditationView(HttpResponse):
    @login_required(login_url="/login/")
    def index(request, pk):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=10)
        ac = accreditation.objects.get(id=pk)

        context = {'segment': 'business', 'sidebars': sidebar, 'title': title, 'page':'Empresas', 'accreditation': ac}
        html_template = loader.get_template('accreditation/view.html')
        return HttpResponse(html_template.render(context, request))

class accreditationUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = accreditation
    template_name = 'accreditation/update.html'
    form_class = accreditationsForm
    success_url = reverse_lazy('accreditation.index')

    def get_context_data(self, **kwargs):
        context = super(accreditationUpdate, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['page'] = 'Actualizar acreditacion'
        context['pk'] = self.kwargs['pk']
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))