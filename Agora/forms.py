from django import forms

class RegForm(forms.Form):
	Email = forms.CharField(placeholder='Email', max_length=100)
    Name = forms.CharField(placeholder='Name', max_length=100)
    Phone = forms.CharField(placeholder='Phone Number', max_length=100)
    Passwrd = forms.CharField(placeholder='Password', max_length=100)
    
