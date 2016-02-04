from django import forms

class SignUp(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True}))
    Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}))
    PhoneNum = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'required': True}))
    Password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))


