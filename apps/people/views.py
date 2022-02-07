# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.people.models import people
from apps.includes.sidebar.models import Sidebar
from apps.people.forms import PeopleForm
# Create your views here.

@login_required(login_url="/login/")
def index(request):

    peoples = people.objects.all()
    sidebar = Sidebar.objects.all()
    if request.method == "POST":
        form = PeopleForm(request.POST, request.FILES)
        if form.is_valid():
            dni = form.cleaned_data.get("dni")
            name = form.cleaned_data.get("name")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            birth_date = form.cleaned_data.get("birth_date")
            address = form.cleaned_data.get("address")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            user_photo_path = form.cleaned_data.get("user_photo_path")
            sex = form.cleaned_data.get("sex")
            user = form.cleaned_data.get("user")
            geographic_location = form.cleaned_data.get("geographic_location")
            marial_status = form.cleaned_data.get("marial_status")
            status = form.cleaned_data.get("status")

            obj = people.objects.create(
                                    dni = dni,
                                    name = name,
                                    first_name = first_name,
                                    last_name = last_name,
                                    birth_date = birth_date,
                                    address = address,
                                    phone = phone,
                                    email = email,
                                    user_photo_path = user_photo_path,
                                    sex = sex,
                                    user = user,
                                    geographic_location = geographic_location,
                                    marial_status = marial_status,
                                    status = status
                                )
            obj.save()
        else:
            messages.error(request, form)
        return redirect('people.index')
    else:
        form = PeopleForm()

    context = {'segment': 'people', 'sidebars': sidebar, 'peoples': peoples, 'title': 'Usuarios', 'forms':form, 'page':'/usuarios'}
    html_template = loader.get_template('people/index.html')
    return HttpResponse(html_template.render(context, request))

def view(request, key_id):
    peoples = people.objects.all()
    sidebar = Sidebar.objects.all()
    context = {'segment': 'people', 'sidebars': sidebar, 'peoples': key_id, 'title': 'Usuarios', 'page':'usuario/perfil'}
    html_template = loader.get_template('people/profile.html')
    return HttpResponse(html_template.render(context, request))