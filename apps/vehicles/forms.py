from django import forms

from apps.vehicles.models import vehicles

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
            'mark' : forms.TextInput(attrs={'class':'form-control form-control-md'}),
            'model' : forms.TextInput(attrs={'class':'form-control form-control-md'}),
            'year_of_production' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'longitude' : forms.TextInput(attrs={'class':'form-control', 'type': 'number'}),
            'height' : forms.TextInput(attrs={'class':'form-control', 'type' : 'number'}),
            'broad' : forms.TextInput(attrs={'class':'form-control', 'type': 'number'}),
            'service_door' : forms.TextInput(attrs={'class':'form-control', 'type' : 'number'}),
            'type' : forms.Select(attrs={'class':'form-control w-50'}),
            'category' : forms.TextInput(attrs={'class':'form-control'}),
            'comment' : forms.Textarea(attrs={'class':'form-control', 'rows' : '3'}),
            'business' : forms.Select(attrs={'class':'form-control w-80'}),
            'terms' : forms.Textarea(attrs={'class':'form-control', 'rows' : '3'}),
            'status' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }