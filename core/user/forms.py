from django.forms import *
from core.user.models import User

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus']= True

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username' : TextInput(attrs={'class':'form-control  form-control-lg', 'autocomplete': 'off'}),
            'password' : PasswordInput(attrs={'class':'form-control  form-control-lg'}),
            'first_name' : TextInput(attrs={'class':'form-control  form-control-sm', 'autocomplete': 'off'}),
            'last_name' : TextInput(attrs={'class':'form-control  form-control-sm', 'autocomplete': 'off'}),
            'email' : TextInput(attrs={'class':'form-control  form-control-sm', 'autocomplete': 'off', 'type': 'email'}),
            'dni' : TextInput(attrs={'class':'form-control  form-control-sm', 'autocomplete': 'off'}),
            'phone' : TextInput(attrs={'class':'form-control  form-control-sm', 'autocomplete': 'off'}),
            'address' : TextInput(attrs={'class':'form-control  form-control-sm', 'autocomplete': 'off'}),
            'user_photo_path' : FileInput(attrs={'class':'form-control  form-control-sm'}),
            'is_staff' : CheckboxInput(attrs={'class' : 'form-check-input'}),
            'is_active' : CheckboxInput(attrs={'class' : 'form-check-input'})
        }
        exclude = ['groups', 'user_permissions', 'last_login', 'is_superuser']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data