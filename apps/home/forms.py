from django import forms
from apps.home.models import Consulting

class ConsultingForm(forms.ModelForm):
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Consulting

        fields = '__all__'

        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control'}),
        }