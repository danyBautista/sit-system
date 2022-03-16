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
            'license_plate',
            'route',
            'score',
            'property_card',
            'seniority_period',
            'soat',
            'soat_status',
            'citv',
            'citv_status',
            'src',
            'src_status',
            'svct',
            'svct_status',
            'RRPP_Newsletter',
            'owner',
            'contract',
            'bonding_contract',
            'enabled',
            'vehicle_authorization',
            'check_sistran',
            'due_date',
            'status',
            'authorization'
        ]
        widgets = {
            'proceedings' : forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'check_date' : forms.TextInput(attrs={'class':'form-control  form-control-sm', 'type': 'date'}),
            'route' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'due_date':forms.TextInput(attrs={'class':'form-control  form-control-sm', 'type': 'date'}),
            'license_plate' : forms.TextInput(attrs={'type':'hidden'}),
            'score' : forms.TextInput(attrs={'type':'hidden'}),
            'property_card' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'seniority_period' : forms.TextInput(attrs={'type':'hidden'}),
            'soat' : forms.TextInput(attrs={'type':'hidden'}),
            'soat_status' : forms.TextInput(attrs={'type':'hidden'}),
            'citv' : forms.TextInput(attrs={'type':'hidden'}),
            'citv_status' : forms.TextInput(attrs={'type':'hidden'}),
            'src' : forms.TextInput(attrs={'type':'hidden'}),
            'src_status' : forms.TextInput(attrs={'type':'hidden'}),
            'svct' : forms.TextInput(attrs={'type':'hidden'}),
            'svct_status' : forms.TextInput(attrs={'type':'hidden'}),
            'RRPP_Newsletter' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'owner' : forms.TextInput(attrs={'type':'hidden'}),
            'contract' : forms.TextInput(attrs={'type':'hidden'}),
            'bonding_contract' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'enabled' : forms.TextInput(attrs={'type':'hidden'}),
            'vehicle_authorization' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'check_sistran' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'authorization' : forms.TextInput(attrs={'type':'hidden'})
        }