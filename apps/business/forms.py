from cProfile import label
from dataclasses import field
from django import forms

from apps.business.models import business

class BusinessForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = business

        fields = [
            'ruc',
            'business_name',
            'address',
            'phone',
            'webpage',
            'registration_date',
            'opening_date',
            'logo_small_path',
            'logo_large_path',
            'business_description',
            'geographic_location',
            'economic_activitie',
            'status'
        ]

        labels = {
            'ruc' :'RUC',
            'business_name' :'Razon social',
            'address': 'Direccion',
            'phone' : 'Telefono',
            'webpage': 'pagina web',
            'registration_date' : 'Fecha de registro',
            'opening_date' : 'Fecha de apertura',
            'logo_small_path': 'Logo pequeño',
            'logo_large_path': 'Log Grande',
            'business_description': 'Descripcion',
            'geographic_location': 'Ubicacion geografica',
            'economic_activitie':'Actividad Economica',
            'status':'Estado'
        }

        widgets = {
            'ruc' : forms.TextInput(attrs={'class':'form-control  form-control-sm', 'type':'number'}),
            'business_name' : forms.TextInput(attrs={'class':'form-control text-uppercase form-control-lg'}),
            'address' : forms.TextInput(attrs={'class':'form-control text-uppercase form-control-sm'}),
            'phone' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'webpage' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'registration_date' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'type':'date'}),
            'opening_date': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type':'date'}),
            'logo_small_path': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Logo pequeño'}),
            'logo_large_path': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Logo grande'}),
            'geographic_location': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'economic_activitie': forms.SelectMultiple(attrs={'class':'form-control select-single'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input mt-2', 'placeholder':'estado'}),
            'business_description': forms.Textarea(attrs={'class':'form-control text-uppercase', 'rows':4})
        }