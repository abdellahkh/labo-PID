from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Select


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, label='Prénom', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, label='Nom', widget=forms.TextInput(attrs={'class':'form-control'}))
    LANGUE_CHOICES = [
    ('FR', 'Français'),
    ('NL', 'Néerlandais'),
    ('EN', 'Anglais'),
    ('DE', 'Allemand'),
    ('AR', 'Arabe'),
]

    langue = forms.ChoiceField(choices=LANGUE_CHOICES, widget=Select(attrs={'class':'form-control'}))


    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'langue', 'password1', 'password2' )

    def __init__(self, *args, **kwargs): 
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['langue'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = 'Mot de passe'
        self.fields['password2'].label = 'Confirmation du mot de passe'
    