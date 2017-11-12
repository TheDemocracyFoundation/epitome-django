from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User



class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
			'username' : forms.TextInput(attrs={'name': 'login-name', 'required': True}),
			'password' : forms.PasswordInput(attrs={'max_length': '64', 'name': 'password', 'required': True}),
        }
        
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control','name': 'name', 'required': True}),
			'email' : forms.EmailInput(attrs={'class':'form-control mt-2','name': 'email', 'required': True}),
			'password' : forms.PasswordInput(attrs={'class':'form-control mt-2','name': 'password', 'required': True}),
       }
