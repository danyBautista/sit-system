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
            'is_active' : CheckboxInput(attrs={'class' : 'form-check-input'}),
            'profile' : Select(attrs={'class': 'form-control select2', 'style': 'width: 90%'}),
            'groups' : SelectMultiple(attrs={'class': 'form-control select2', 'style': 'width: 90%'})
        }
        exclude = ['user_permissions', 'last_login', 'is_superuser']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()

                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data