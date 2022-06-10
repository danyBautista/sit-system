from django import forms

from django.contrib.auth.models import User

class PeopleForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined'
        ]