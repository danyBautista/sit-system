# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present GlastHeim.pe
"""
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

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
from .serializers import PeopleSerializer
# Create your views here.

@login_required(login_url="/login/")
def index(request):

    peoples = people.objects.all()
    sidebar = Sidebar.objects.all()
    title = Sidebar.objects.get(id="3")
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
            profile_information = form.cleaned_data.get("profile_information")
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
                                    profile_information = profile_information,
                                    marial_status = marial_status,
                                    status = status
                                )
            obj.save()
        else:
            messages.error(request, form)
        return redirect('people.index')
    else:
        form = PeopleForm()

    context = {'segment': 'people', 'sidebars': sidebar, 'peoples': peoples, 'title': title, 'forms':form, 'page':'/usuarios'}
    html_template = loader.get_template('people/index.html')
    return HttpResponse(html_template.render(context, request))

def view(request, key_id):
    user = people.objects.get(dni=key_id)
    sidebar = Sidebar.objects.all()
    context = {'segment': 'people', 'sidebars': sidebar, 'people': user, 'title': 'Usuarios', 'page':'usuario/perfil'}
    html_template = loader.get_template('people/profile.html')
    return HttpResponse(html_template.render(context, request))

""" services start here """

class PeopleListAPIView(ListAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', '')
        return people.objects.filter(name__icontains = kword)

class PeopleUpdateAPIView(UpdateAPIView):
    serializer_class = PeopleSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(status = True).filter(dni = pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            PeopleSerializer = self.serializer_class(self.get_queryset(pk))
            return Response(PeopleSerializer.data)
        return Response({'error':'No existe usuario con estos datos!'})

    def put(self, request, pk=None):

        if self.get_queryset(pk):
            PeopleSerializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if PeopleSerializer.is_valid():
                PeopleSerializer.save()
                return Response(PeopleSerializer.data)
            return Response(PeopleSerializer.errors)