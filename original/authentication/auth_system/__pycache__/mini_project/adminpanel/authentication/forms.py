from django import forms
from crud.models import  UserProfile



class UserSignin(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        widgets = {
                    'username' : forms.TextInput(attrs={'class':'form-control col-12'}),
                    'password' : forms.PasswordInput(render_value=True,attrs={'class':'form-control col-12' } )
                }



class UserSignup(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'password', 'Confirm_password']
        widgets = {
                    'username' : forms.TextInput(attrs={'class':'form-control col-12'}),
                    'first_name' : forms.TextInput(attrs={'class':'form-control col-12'}),
                    'last_name' : forms.TextInput(attrs={'class':'form-control col-12'}),
                    'password' : forms.PasswordInput(render_value=True ,attrs={'class':'form-control col-12'}),
                    'Confirm_password' : forms.PasswordInput(render_value=True ,attrs={'class':'form-control col-12' })
                }