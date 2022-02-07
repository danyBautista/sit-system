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
            'user_photo_path',
            'sex',
            'user',
            'geographic_location',
            'marial_status',
            'status'
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
            'user': 'Usuario de sistem',
            'geographic_location' : 'Ubiego',
            'marial_status' : 'Estado civil',
            'status' : 'estado'
        }
        widgets = {
            'dni' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'DNI'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Completo'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido materno'}),
            'birth_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Fecha de nacimiento', 'type':'date'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Correo Electronico'}),
            'user_photo_path': forms.FileInput(attrs={'class':'form-control'}),
            'sex' : forms.Select(attrs={'class':'form-control'}),
            'user' : forms.Select(attrs={'class':'form-control', 'placeholder':'Usuario de sistema'}),
            'geographic_location': forms.Select(attrs={'class':'form-control','placeholder':'UbiGeo'}),
            'marial_status': forms.Select(attrs={'class':'form-control','placeholder':'Estado civil'}),
            'status': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }