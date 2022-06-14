from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.includes.sidebar.models import Sidebar

# Create your views here.
class HomeIndex(HttpResponse):
    @login_required(login_url='/login/')
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=8)

        context = {'segment': 'report', 'sidebars': sidebar, 'title': title, 'page':'Reportes'}
        html_template = loader.get_template('reports/index.html')
        return HttpResponse(html_template.render(context, request))