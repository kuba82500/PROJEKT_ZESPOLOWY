from django import forms
from .models import Praktyki
from django.forms import ModelForm


class StworzPraktyke(ModelForm):
    DataZakonczenia = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'placeholder': 'YYYY-MM-DD',
            'class': 'form-control'
        }
    ))
    DataRozpoczecia = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'placeholder': 'YYYY-MM-DD',
            'class': 'form-control'
        }
    ))
    opis = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows': '10',
            'cols': '100',
            'class': 'form-control'
        }
    ))
    miasto = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    stanowisko = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    wynagrodzenie = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Praktyki
        fields = [
            'DataZakonczenia', 'DataRozpoczecia', 'miasto', 'stanowisko', 'opis', 'wynagrodzenie',
        ]

        widgets = {
            'id_Firma': forms.HiddenInput(),
        }
