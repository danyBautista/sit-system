# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present glastheim.pe
"""

from dataclasses import fields
from django import forms

from apps.certify.models import soat, citv, src, svct

class SOATForm(forms.ModelForm):
    class Meta:
        model = soat

        fields = [
            'policy',
            'certify',
            'insurance_company',
            'number',
            'registration_date',
            'date_expiry',
            'category',
            'vin_serie',
            'insured',
            'amount',
            'file',
            'vehicles',
            'owners',
            'status'
        ]
        labels = {
            'policy':'N° de Polisa de seguros',
            'certify':'Certificado',
            'insurance_company':'Compañia de seguros',
            'number':'Numero',
            'registration_date':'Fecha de registro',
            'date_expiry':'Fecha de expiracion',
            'category':'Categoria',
            'vin_serie':'N° VIN',
            'insured':'asegurada',
            'amount':'Monto',
            'file':'Archivo',
            'vehicles':'Vehiculo',
            'owners':'Propietarios',
            'status':'Estado'
        }
        widgets = {
            'policy' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'certify': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'insurance_company': forms.Select(attrs={'class':'form-control form-control-sm select-single', 'style': 'width:100%'}),
            'number': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'registration_date': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'date_expiry': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'vin_serie': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'insured': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'amount': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'file': forms.FileInput(attrs={'class':'form-control'}),
            'owners': forms.CheckboxSelectMultiple(),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class CITVForm(forms.ModelForm):
    class Meta:
        model = citv

        fields = [
            'id',
            'Registration_date',
            'expiration_date',
            'inspection_result',
            'comment',
            'Type_of_inspection',
            'file',
            'vehicle',
            'type_service',
            'scope',
            'status'
        ]
        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'Registration_date': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'expiration_date':forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'inspection_result': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'comment' : forms.Textarea(attrs={'class':'form-control', 'rows': 3, 'placeholder': 'Comentarios'}),
            'Type_of_inspection': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'file' : forms.FileInput(attrs={'class':'form-control'}),
            'type_service': forms.Select(attrs={'class':'form-control'}),
            'scope': forms.Select(attrs={'class':'form-control'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class SRCForm(forms.ModelForm):
    class Meta:
        model = src

        fields = {
            'name',
            'registration_date',
            'date_expiry',
            'file',
            'vehicles',
            'status'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'registration_date': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'date_expiry': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'file': forms.FileInput(attrs={'class':'form-control'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }

class SVCTForm(forms.ModelForm):
    class Meta:
        model = svct

        fields = {
            'name',
            'registration_date',
            'date_expiry',
            'file',
            'vehicles',
            'status'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'registration_date': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'date_expiry': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type': 'date'}),
            'file': forms.FileInput(attrs={'class':'form-control'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }