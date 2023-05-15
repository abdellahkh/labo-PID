from django.core import validators
from django import forms
from .models import Artist, Show

from .models import Locality

class ShowRegistration(forms.ModelForm):
    class Meta:
        model = Show 
        fields = [ 'slug', 'title', 'description', 'poster_url', 'location_id', 'bookable', 'price' ]
        widgets = {   #@TODO
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'poster_url': forms.TextInput(attrs={'class': 'form-control'}),
            'location_id': forms.TextInput(attrs={'class': 'form-control'}),
            'bookable': forms.CheckboxInput(attrs={'class': 'form-control'}), 
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ArtistFormCreation(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['firstname','lastname']


class ArtistDeleteForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = []
        


class LocalityFormCreation(forms.ModelForm):
    class Meta:
        model = Locality
        fields = ['postal_code', 'locality']
