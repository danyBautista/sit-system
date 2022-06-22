from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from apps.accreditation.models import accreditation

from apps.includes.sidebar.models import Sidebar

# Create your views here.
class HomeIndex(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=9)
        context = {'segment': 'report', 'sidebars': sidebar, 'title': title, 'page':'Reportes'}
        html_template = loader.get_template('reports/index.html')
        return HttpResponse(html_template.render(context, request))

class AccreditationReports(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = accreditation
    template_name = 'reports/accreditations.html'

    def get_context_data(self, **kwargs):
        context = super(AccreditationReports, self).get_context_data(**kwargs)
        context['segment'] = 'report'
        context['sidebars'] = Sidebar.objects.all()
        context['title'] = Sidebar.objects.get(id=9)
        context['page'] = 'Generar roportes'
        context['accreditation'] = accreditation.objects.all().filter(type__name = self.kwargs['tp'])
        context['table_title'] = self.kwargs['tp']
        return context