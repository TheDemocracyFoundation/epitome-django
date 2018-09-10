from django import forms
from django.forms import ModelForm, Textarea, modelform_factory, modelformset_factory
from Demoscopesis.models import Poll, PollChoice
#from django.utils import timezone

class PollForm(ModelForm):
	class Meta:
		model = Poll
		fields = ('PL_TITLE', 'PL_SHRBODY', 'PL_BODY', 'PL_STARTDT', 'PL_ENDDT', 'POLLCAT')
		widgets = {
			'PL_TITLE' : forms.TextInput(attrs={'type':'text','id':'title','class':'form-control','required': True, 'autofocus': True}),
			'PL_SHRBODY' : Textarea(attrs={'id':'shortbody','class':'form-control','rows':'3', 'required': True}),
			'PL_BODY' : Textarea(attrs={'id':'body','class':'form-control','rows':'10', 'required': True}),
			'PL_STARTDT' : forms.TextInput(attrs={'type':'date','id':'startdate','class':'form-control','required': True}),
			'PL_ENDDT' : forms.TextInput(attrs={'type':'date','id':'enddate','class':'form-control','required': True}),
			'PL_STIME' : forms.TextInput(attrs={'type':'text','id':'stime','class':'form-control','required': True}),
			#'POLLCAT' : forms.TextInput(attrs={'type':'text','id':'form-categories','class':'form-control', 'style':'display:none' ,'required': True})
			'POLLCAT' : forms.CheckboxSelectMultiple()
		}
	
	#def __init__(self, *args, **kwargs):
		#self.request = kwargs.pop("request")
		#super(PollForm, self).__init__(*args, **kwargs)
		#self.fields['USER'].initial = self.request.user.id
		#self.fields['PL_CREATION'].initial = timezone.now

class PollChoiceForm(ModelForm):
	class Meta:
		model = PollChoice
		fields = ('PC_CHOICE',) # Fields is not a String, comma is needed.
		widgets = {
			'PC_CHOICE' : forms.TextInput(attrs={'type':'hidden', 'id':'payload' ,'class':'form-control','required': True})
		}
		
#PollChoiceFormSet = modelformset_factory(PollChoice, form=PollChoiceForm, extra=2)



PollChoiceFormSet = modelformset_factory(
    PollChoice,
    fields=('PC_CHOICE', ),
    extra=2,
    widgets={'PC_CHOICE': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter choice here'
        })
    }
)