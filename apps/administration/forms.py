from django import forms

from django.contrib.auth.models import User
from apps.administration.models import profiles
class PeopleForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined'
        ]

class ProfilesForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = profiles

        fields = ['profile_name', 'route', 'status']

        widgets = {
            'profile_name' : forms.TextInput(attrs={'class':'form-control  form-control-lg'}),
            'route' : forms.TextInput(attrs={'class':'form-control  form-control-sm'}),
            'status':forms.CheckboxInput(attrs={'class':'form-check-input mt-2', 'placeholder':'estado'}),
        }