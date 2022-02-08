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
            'ruc' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'RUC'}),
            'business_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Razon social'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}),
            'webpage' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pagina Web'}),
            'registration_date' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fecha de registro', 'type':'date'}),
            'opening_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fecha de apertura', 'type':'date'}),
            'logo_small_path': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Logo pequeño'}),
            'logo_large_path': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Logo grande'}),
            'geographic_location': forms.Select(attrs={'class':'form-control', 'placeholder':'Localizacion geografica'}),
            'economic_activitie': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'actividad econocica'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input', 'placeholder':'estado'}),
            'business_description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Descripcion'})
        }