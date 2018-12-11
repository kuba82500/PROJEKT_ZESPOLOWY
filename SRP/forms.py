from django import forms
from .models import Uzytkownik, Praktyki
from django.forms import ModelForm


class RegisterForm(ModelForm):
    haslo = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Uzytkownik
        fields = ['numerIndeksu', 'imie', 'nazwisko', 'email', 'haslo', ]


class StworzPraktyke(ModelForm):
    class Meta:
        model = Praktyki
        exclude = ['']
