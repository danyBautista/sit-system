from django import forms

from apps.validations.models import binding_contracts, procedure, routes, vehicle_substitution, authorization_documents

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
class binding_contractsForm(forms.ModelForm):
    class Meta:
        model = binding_contracts
        fields = [
            'code',
            'registration_date',
            'due_date',
            'document',
            'status',
        ]
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'registration_date': forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off', 'type':'date'}),
            'due_date': forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off', 'type':'date'}),
            'document': forms.FileInput(attrs={'class':'form-control'}),
            'status' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
class autauthorization_documents_form(forms.ModelForm):
    class Meta:
        model = authorization_documents
        fields = [
            'code',
            'enabled',
            'file',
            'status',
            'commnet',
        ]
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control form-control-lg', 'autocomplete': 'off'}),
            'enabled' : forms.Select(attrs={'class':'form-control form-control-sm'}),
            'file' : forms.FileInput(attrs={'class':'form-control form-control-sm'}),
            'status' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'commnet' : forms.Textarea(attrs={'class':'form-control', 'rows' : 5, 'placeholder': 'Comentario'}),
        }
class SubstitutionForm(forms.ModelForm):
    class Meta:
        model = vehicle_substitution
        fields = [
            'sustitucion',
            'exit_ticket',
            'plate',
            'vehicle_authorization_document',
            'file_authorization'
        ]
        widgets = {
            'sustitucion' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'exit_ticket' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'plate': forms.Select(attrs={'class':'form-check-input select-sustit'}),
            'vehicle_authorization_document' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'file_authorization' : forms.FileInput(attrs={'class':'form-control'})
        }

class ProcedureForm(forms.ModelForm):
    class Meta:
        model = procedure
        fields = [
            'proceedings',
            'year_proceeding',
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
            'authorization',
            'years',
            'substitution'
        ]
        widgets = {
            'proceedings' : forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'year_proceeding' : forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'license_plate' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'check_date' : forms.TextInput(attrs={'class':'form-control  form-control-sm', 'type': 'date'}),
            'route' : forms.Select(attrs={'class':'form-control w-80 form-control-sm select-single'}),
            'score' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
            'property_card' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'seniority_period' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'soat' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'soat_status' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'citv' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'citv_status' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'src' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'src_status' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'svct' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'svct_status' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'RRPP_Newsletter' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'owner' : forms.SelectMultiple(attrs={'class':'form-control  form-control-sm'}),
            'contract' : forms.Select(attrs={'class':'form-control w-80 form-control-sm select-single d-flex'}),
            'bonding_contract' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'enabled' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'vehicle_authorization' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'check_sistran' : forms.CheckboxInput(attrs={'class':'form-check-input mb-0'}),
            'due_date':forms.TextInput(attrs={'class':'form-control  form-control-sm', 'type': 'date'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'authorization' : forms.Select(attrs={'class':'form-control form-control-sm w-70 select-single'}),
            'years' : forms.Select(attrs={'class': 'form-control  form-control-sm select-single'}),
            'substitution' : forms.Select(attrs={'class': 'form-control w-70 form-control-sm select-single'}),
        }