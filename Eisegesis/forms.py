from django import forms
from django.forms import ModelForm
from Eisegesis.models import Poll

class PollForm(ModelForm):
    model = Poll
    fields = ('Title', 'Body')
    widgets = {
        'Title' : forms.TextInput(attrs={'type':'text','id':'Title','class':'form-control','placeholder':'Title','name': 'Title', 'required': True, 'autofocus':True}),
        'Body' : forms.TextInput(attrs={'type':'text','id':'Body','class':'form-control mt-3','placeholder':'Body','name': 'Body', 'required': True}),
    }