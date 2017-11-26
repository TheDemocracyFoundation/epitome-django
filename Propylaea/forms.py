from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User



class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
			'username' : forms.TextInput(attrs={'type':'text','id':'username', 'class':'form-control','placeholder':'Username','name': 'username', 'required': True, 'autofocus':True}),
			'password' : forms.PasswordInput(attrs={'type':'password','id':'inputPassword','class':'form-control mt-3','placeholder':'Password','max_length': '64', 'name': 'password', 'required': True})
        }
        
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
			'username' : forms.TextInput(attrs={'type':'text','id':'username','class':'form-control','placeholder':'Username','name': 'username', 'required': True, 'autofocus':True}),
			'email' : forms.EmailInput(attrs={'type':'text','id':'email','class':'form-control mt-3','placeholder':'e-mail','name': 'email', 'required': True}),
			'password' : forms.PasswordInput(attrs={'type':'password','id':'inputPassword','class':'form-control mt-3','placeholder':'Password','name': 'password', 'required': True}),
       }
