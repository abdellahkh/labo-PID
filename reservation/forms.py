from django.core import validators
from django import forms
from .models import Show

class ShowRegistration(forms.ModelForm):
    class Meta:
        model = Show 
        fields = [ 'slug', 'title', 'description', 'poster_url', 'locality_id', 'bookable', 'price' ]
        widgets = {   #@TODO
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'poster_url': forms.TextInput(attrs={'class': 'form-control'}),
            'locality_id': forms.TextInput(attrs={'class': 'form-control'}),
            'bookable': forms.CheckboxInput(attrs={'class': 'form-control'}), 
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }