from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User



class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
			'username' : forms.TextInput(attrs={'name': 'name', 'required': True}),
			'password' : forms.PasswordInput(attrs={'max_length': '64', 'name': 'password', 'required': True}),
        }
        
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
			'username' : forms.TextInput(attrs={'name': 'name', 'required': True}),
			'email' : forms.EmailInput(attrs={'name': 'email', 'required': True}),
			'password' : forms.PasswordInput(attrs={'name': 'password', 'required': True}),
        }
