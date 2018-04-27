from django import forms
from django.forms import ModelForm, Textarea
from Demoscopesis.models import Poll

class PollForm(ModelForm):
	class Meta:
		model = Poll
		fields = ('PL_TITLE', 'PL_BODY')
		widgets = {
			'PL_TITLE' : Textarea(attrs={'id':'Title','class':'form-control','rows':'10', 'required': True, 'autofocus':True}),
			'PL_BODY' : forms.TextInput(attrs={'type':'text','id':'Body','class':'form-control mt-3','placeholder':'Body', 'required': True}),
		}
