from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from Propylaea.models import UserExtra

class UserFormExtra(ModelForm):   
    class Meta:
        model = UserExtra
        fields = ('phoneNumber',)
        widgets = {
			'phoneNumber' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'required': False}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
			'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
			'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True}),
			'password' : forms.PasswordInput(attrs={'max_length': '32', 'class': 'form-control', 'placeholder': 'Password', 'required': True}),
        }

