from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.accreditation.forms import accreditationsForm
from apps.accreditation.models import accreditation
from apps.includes.sidebar.models import Sidebar
# Create your views here.

class accreditationView(ListView):
    model = accreditation
    template_name  = 'accreditation/index.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(accreditationView, self).get_context_data(**kwargs)
        context['segment'] = 'accreditation'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=10)
        context['page'] = 'Crear Propietario'
        return context

class accreditationCreate(CreateView):
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