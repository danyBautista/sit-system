from django import forms

from apps.people.models import people

class PeopleForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = people
        fields = [
            'dni',
            'name',
            'first_name',
            'last_name',
            'birth_date',
            'address',
            'phone',
            'email',
            'sex',
            'geographic_location',
            'marial_status',
            'status',
            'profile_information'
        ]
        labels = {
            'dni' : 'DNI',
            'name' : 'Nombre completo',
            'first_name' : 'Apellido Paterno',
            'last_name':'Apellido manterno',
            'birth_date':'Fecha de nacimiento',
            'address':'Direccion',
            'phone':'telofono',
            'email': 'Correo electronico',
            'user_photo_path' : 'Imagen de usuario',
            'sex' : 'Sexo',
            'geographic_location' : 'Ubiego',
            'marial_status' : 'Estado civil',
            'status' : 'estado',
            'profile_information': 'Informacion de perfil'
        }
        widgets = {
            'dni' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'birth_date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'address': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'phone': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'email': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'user_photo_path': forms.FileInput(attrs={'class':'form-control'}),
            'sex' : forms.Select(attrs={'class':'form-control form-control-sm'}),
            'geographic_location': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'marial_status': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'profile_information': forms.Textarea(attrs={'class':'form-control'})
        }