import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from apps.includes.sidebar.models import Sidebar
from apps.business.forms import BusinessForm
from apps.business.models import business
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')
class ListView(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=4)
        context = {'segment': 'validate', 'sidebars': sidebar, 'title': title, 'page':'Empresas'}
        html_template = loader.get_template('business/index.html')
        return HttpResponse(html_template.render(context, request))

class BusinessCreate(HttpResponse):
    def index(request):
        sidebar = Sidebar.objects.all()
        title = Sidebar.objects.get(id=4)

        if request.method == "POST":
            form = BusinessForm(request.POST, request.FILES)
            if form.is_valid():
                ruc= form.cleaned_data.get('ruc')
                business_name= form.cleaned_data.get('business_name')
                address= form.cleaned_data.get('address')
                phone= form.cleaned_data.get('phone')
                webpage= form.cleaned_data.get('webpage')
                registration_date= form.cleaned_data.get('registration_date')
                opening_date= form.cleaned_data.get('opening_date')
                logo_small_path= form.cleaned_data.get('logo_small_path')
                logo_large_path= form.cleaned_data.get('logo_large_path')
                business_description= form.cleaned_data.get('business_description')
                geographic_location= form.cleaned_data.get('geographic_location')
                economic_activitie= form.cleaned_data.get('economic_activitie')
                status= form.cleaned_data.get('status')
                obj = business.objects.create(
                    ruc = ruc,
                    business_name = business_name,
                    address = address,
                    phone = phone,
                    webpage = webpage,
                    registration_date = registration_date,
                    opening_date = opening_date,
                    logo_small_path = logo_small_path,
                    logo_large_path = logo_large_path,
                    business_description = business_description,
                    geographic_location = geographic_location,
                    economic_activitie = economic_activitie,
                    status = status
                )
                obj.save()
            else:
                messages.error(request, form)
            return redirect('business.index')
        else:
            form = BusinessForm()

        context = {'segment': 'vehicles', 'sidebars': sidebar, 'title': title, 'page':'Empresas', 'form' : form}
        html_template = loader.get_template('business/create.html')
        return HttpResponse(html_template.render(context, request))