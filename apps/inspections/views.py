from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.vehicles.models import vehicles
from apps.accreditation.models import accreditation, accreditation_type
from apps.validations.models import procedure
# Create your views here.

class index(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = "inspections/index.html"

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['title'] = 'Fiscalizacion'
        return context

class SearchView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'inspections/search.html'

    def get_percent_accreditation(self):
        percent = 0
        try:
            accre = accreditation.objects.get(plate = self.kwargs['key'])
            if(accre.legal_requirements == 'CUMPLE'):
                percent = percent + 20
            if(accre.technical_requirements == 'CUMPLE'):
                percent = percent + 20
            if(accre.technical_requirements == 'CUMPLE'):
                percent = percent + 20
            if(accre.insurance == 'CUMPLE'):
                percent = percent + 20
            if(accre.accreditation_card == True):
                percent = percent + 20
            return percent
        except accreditation.DoesNotExist:
            accre = None
        return accre

    def get_percent_validation(self):
        percent = 0
        #vali = procedure.objects.get(license_plate = self.kwargs['key']).first()

        return percent

    def get_certification(self):
        try:
            v_soat = soat.objects.all().filter(vehicles = self.kwargs['key'], status = True).first()
            v_citv = citv.objects.all().filter(vehicle = self.kwargs['key'], status = True).first()
            v_src = src.objects.all().filter(vehicles = self.kwargs['key'], status = True).first()
            v_svct = svct.objects.all().filter(vehicles = self.kwargs['key'], status = True).first()
            certify = {'soat' : v_soat, 'citv' : v_citv, 'src' : v_src, 'svct' : v_svct}
        except:
            certify = None
        return certify

    def get_validation(self):
        try:
            accr = procedure.objects.get(license_plate = self.kwargs['key'])
        except procedure.DoesNotExist:
            accr = None
        return accr

    def get_accreditation(self):
        try:
            accr = accreditation.objects.get(plate = self.kwargs['key'])
        except accreditation.DoesNotExist:
            accr = None
        return accr

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['segment'] = 'index'
        context['title'] = 'Verificar'
        context['vehicle'] = vehicles.objects.get(plate = self.kwargs['key'])
        context['accreditation'] = self.get_accreditation()
        context['percent_accreditation'] = self.get_percent_accreditation()
        context['certify'] = self.get_certification()
        context['validation'] = self.get_validation()
        context['percent_validaiton'] = self.get_percent_validation()
        context['page'] = 'Crear Acreditacion'
        return context