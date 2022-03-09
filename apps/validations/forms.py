from django import forms

from apps.validations.models import routes

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