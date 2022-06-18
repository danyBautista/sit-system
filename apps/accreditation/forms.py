from django import forms

from apps.accreditation.models import accreditation, accreditation_type
class typeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus']= True
    class Meta:
        model = accreditation_type

        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'description' : forms.TextInput(attrs={'class':'form-control  form-control-sm', 'autocomplete': 'off'}),
            'status' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            'color' : forms.Select(attrs={'class' : 'form-control  form-control-sm select-single'})
        }


class accreditationsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['permit_number'].widget.attrs['autofocus']= True

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
            'type',
            'enabled'
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
            'permit_number': forms.TextInput(attrs={'class':'form-control form-control-lg', 'autocomplete': 'off'}),
            'remark' : forms.Textarea(attrs={'class':'form-control', 'rows' : '5'}),
            'bussines' : forms.Select(attrs={'class':'form-control  form-control-sm select-single'}),
            'status' : forms.Select(attrs={'class':'form-control  form-control-sm'}),
            'type' : forms.Select(attrs={'class':'form-control  form-control-sm select-single', 'style': 'width: 83%'}),
            'enabled' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }