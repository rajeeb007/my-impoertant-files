from django import forms
from .models import  UserProfile
from django.core import validators

class StudentRegistration(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder' : 'Enter Password','class' : 'form-control col-3'}))
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            # 'password' : forms.PasswordInput(render_value=True ,attrs={'class':'form-control col-3'}),
            # 'Confirm_password' : forms.PasswordInput(render_value=True ,attrs={'class':'form-control col-3'})
        }