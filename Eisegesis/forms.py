from django import forms



class VotingOptions(forms.Form):
    """
    Form for individual voting options
    """
    anchor = forms.CharField(
                    max_length=100,
                    widgets = {
                        'pollbody' : forms.TextInput(attrs={
                                'type':'text','id':'username', 'class':'form-control','placeholder':'Username','name': 'username', 'required': True, 'autofocus':True
                            }),
                        'votingoption' : forms.TextInput(attrs={
                                'placeholder': 'Add your voting option here...','class':'form-control'
                            })
                    },
                    required=True)