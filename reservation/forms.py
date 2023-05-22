from django.core import validators
from django import forms
from .models import Artist, RepresentationUser, Show, Representation
from django.contrib.auth.models import User


class ShowRegistration(forms.ModelForm):
    representations = forms.ModelMultipleChoiceField(
        queryset=Representation.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
         required=False
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

    def __init__(self, *args, **kwargs):
        super(ShowRegistration, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Show has already been created, so populate existing representations
            self.fields['representations'].queryset = Representation.objects.filter(show_id=self.instance.pk)
        elif 'location_id' in self.initial:
            # New Show form, filter representations based on location_id
            location_id = self.initial['location_id']
            self.fields['representations'].queryset = Representation.objects.filter(show__isnull=True, location_id=location_id)

    def save(self, commit=True):
        show = super(ShowRegistration, self).save(commit=commit)
        if commit:
            # Assign the show ID to selected representations
            representations = self.cleaned_data['representations']
            for representation in representations:
                representation.show = show
                representation.save()
        return show




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



class RepresentationForm(forms.ModelForm):
    class Meta:
        model = Representation
        fields = ['show_id', 'when', 'location_id']
        widgets = {
            'when': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'}),
        }


class UserRepresentationForm(forms.ModelForm):
    class Meta:
        model = RepresentationUser
        fields = ['representation_id', 'user_id', 'places']
        