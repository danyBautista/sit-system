import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from apps.business.forms import BusinessForm
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    sidebar = Sidebar.objects.all()
    title = Sidebar.objects.get(id=4)

    if request.method == "POST":
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, form)
        return redirect('business.index')
    else:
        form = BusinessForm()

    context = {'segment': 'business', 'sidebars': sidebar, 'title': title, 'page':'Empresas', 'forms':form}
    Http_template = loader.get_template('business/index.html')
    return HttpResponse(Http_template.render(context, request))