from django import forms

from apps.includes.sidebar.models import Sidebar

class SidebarForm(forms.ModelForm):
    class Meta:
        model = Sidebar

        fields = ['__all__']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'route' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'icon' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'group' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'segment' : forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'status' : forms.TextInput(attrs={'class':'form-check-input'}),
            'sub_menu' : forms.Select(attrs={'class':'form-control'})
        }