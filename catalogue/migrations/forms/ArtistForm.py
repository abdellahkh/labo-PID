from django import forms
class ArtistForm(forms.Form):
     firstname = forms.CharField(label='Firstname', max_length=60)
     lastname = forms.CharField(label='Lastname', max_length=60)