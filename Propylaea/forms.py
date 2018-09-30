from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'type': 'text', 'id': 'login-username', 'class': 'form-control', 'placeholder': 'Username',
                       'name': 'username', 'required': True, 'autofocus': True}),
            'password': forms.PasswordInput(
                attrs={'type': 'password', 'id': 'login-password', 'class': 'form-control mt-3',
                       'placeholder': 'Password', 'max_length': '64', 'name': 'password', 'required': True})
        }


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'type': 'text', 'id': 'registration-username', 'class': 'form-control',
                                               'placeholder': 'Username', 'name': 'username', 'required': True,
                                               'autofocus': True, 'style': 'box-shadow: none'}),
            'email': forms.EmailInput(attrs={'type': 'text', 'id': 'registration-email', 'class': 'form-control mt-3',
                                             'placeholder': 'e-mail', 'name': 'email', 'required': True, 'style': 'box-shadow: none'}),
            'password': forms.PasswordInput(
                attrs={'type': 'password', 'id': 'registration-password', 'class': 'form-control mt-3',
                       'placeholder': 'Password', 'name': 'password', 'required': True, 'data-toggle': 'popover',
                       'data-placement': 'right', 'data-content': 'Length must be over 8 characters long',
                       'data-trigger': 'manual', 'style': 'box-shadow: none'}),
        }
