from django.core import validators
from django import forms
from .models import Artist, Show, Representation
from django.contrib.auth.models import User

class ShowRegistration(forms.ModelForm):
    representations = forms.ModelMultipleChoiceField(
        queryset=Representation.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Show 
        fields = ['slug', 'title', 'description', 'poster_url', 'location_id', 'bookable', 'price', 'image', 'representations']
        
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'poster_url': forms.TextInput(attrs={'class': 'form-control'}),
            'location_id': forms.TextInput(attrs={'class': 'form-control'}),
            'bookable': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }



class ArtistFormCreation(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['firstname', 'lastname']
        labels = {
            'firstname': 'Prénom',
            'lastname': 'Nom',
        }
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ArtistDeleteForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = []


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']