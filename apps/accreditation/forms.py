from django import forms

from apps.accreditation.models import accreditation

class accreditationsForm(forms.ModelForm):
    class Meta:
        model = accreditation

        fields = [
            'plate',
            'route',
            'legal_requirements',
            'technical_requirements',
            'mechanical_inspection',
            'insurance',
            'accreditation_card',
            'year_of_production',
            'typology',
            'permit_number',
            'remark',
            'bussines',
            'status',
        ]

        widgets = {
            'plate' : forms.Select(attrs={'class':'form-control w-100 select-single', 'style':'width: 100%'}),
            'route' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'legal_requirements' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
            'technical_requirements' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
            'mechanical_inspection' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
            'insurance' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
            'accreditation_card' : forms.CheckboxInput(attrs={'class':'form-check-input mt-2', 'placeholder':'estado'}),
            'year_of_production' : forms.TextInput(attrs={'class':'form-control  form-control-sm'}),
            'typology' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'permit_number': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'remark' : forms.Textarea(attrs={'class':'form-control', 'rows' : '5'}),
            'bussines' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'status' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
        }