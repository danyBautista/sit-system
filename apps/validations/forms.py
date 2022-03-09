from django import forms

from apps.validations.models import procedure, routes

class RoutesForm(forms.ModelForm):
    class Meta:
        model = routes
        fields = [
            'route',
            'concession',
            'status',
            'limit'
        ]

        labels = {
            'route': 'route',
            'concession': 'concession',
            'status': 'status',
            'limit':'limit'
        }

        widgets = {
            'route' : forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'concession' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'limit' : forms.NumberInput(attrs={'class':'form-control form-control-sm', 'v-model' : 'limit'})
        }

class ProcedureForm(forms.ModelForm):
    class Meta:
        model = procedure
        fields = [
            'proceedings',
            'check_date',
            'id_route',
            'status'
            ]
        widgets = {
            'proceedings' : forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'check_date' : forms.TextInput(attrs={'class':'form-control  form-control-sm', 'type': 'date'}),
            'id_route' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }