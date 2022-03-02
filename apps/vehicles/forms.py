from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms

from apps.vehicles.models import vehicles, types

class VehicleForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = vehicles

        fields = [
            'plate',
            'mark',
            'model',
            'year_of_production',
            'longitude',
            'height',
            'broad',
            'service_door',
            'type',
            'category',
            'comment',
            'business',
            'owners',
            'terms',
            'status',
        ]
        labels = {
            'plate' : 'Placa de rodaje',
            'mark' : 'Marca',
            'model' : 'Modelo',
            'year_of_production' : 'Año de Produccion',
            'longitude' : 'Longitud',
            'height' : 'Alto',
            'broad' : 'Ancho',
            'service_door' : 'Puertas de Servicio',
            'type' : 'Tipo',
            'category' : 'Categoria',
            'comment' : 'Observaciones',
            'business' : 'Empresa',
            'terms' : 'Terminos',
            'status' : 'Estado',
        }
        widgets = {
            'plate' : forms.TextInput(attrs={'class':'form-control  form-control-lg'}),
            'mark' : forms.TextInput(attrs={'class':'form-control  form-control-sm'}),
            'model' : forms.TextInput(attrs={'class':'form-control  form-control-sm'}),
            'year_of_production' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'type':'number'}),
            'longitude' : forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'height' : forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'broad' : forms.NumberInput(attrs={'class':'form-control form-control-sm'}),
            'service_door' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'type' : 'number'}),
            'type' :  forms.Select(attrs={'class':'form-control w-60'}),#AutocompleteSelect(                            vehicles._meta.get_field('type').remote_field,                            admin.site,                            attrs={'class':'form-control form-control-sm w-50'}                        ),
            'category' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'comment' : forms.Textarea(attrs={'class':'form-control', 'rows' : '3'}),
            'business' : forms.Select(attrs={'class':'form-control w-80'}),
            'terms' : forms.Textarea(attrs={'class':'form-control', 'rows' : '3'}),
            'status' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'owners' : forms.CheckboxSelectMultiple(attrs={'class':'form-check-input'})
        }

class TypeVehicleForm():
    class Meta:
        model = types

        fields = [
            'name',
            'status'
        ]
        labels = {
            'name' : 'Nombre',
            'status': 'Estado'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }