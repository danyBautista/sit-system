from django.shortcuts import render

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.includes.sidebar.forms import SidebarForm

from apps.includes.sidebar.models import Sidebar

# Create your views here.
class SidebarList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Sidebar

    template_name  = 'includes/tools/sidebar-list.html'

    def get_context_data(self, **kwargs):
        context = super(SidebarList, self).get_context_data(**kwargs)
        context['segment'] = 'sidebar'
        context['sidebars'] = Sidebar.objects.all()
        context['page'] = 'Crear empresa'
        context['form'] = SidebarForm
        return context