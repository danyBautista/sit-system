from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class index(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = "inspections/index.html"

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['title'] = 'Fiscalizacion'
        return context
