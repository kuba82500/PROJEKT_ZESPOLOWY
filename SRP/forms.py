from django import forms
from .models import Praktyki, Grupa
from django.forms import ModelForm


class StworzPraktyke(ModelForm):
    dataZakonczenia = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD',
        }
    ))
    dataRozpoczecia = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD'
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

    iloscMiejscMax = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Praktyki
        fields = [
            'dataZakonczenia', 'dataRozpoczecia', 'miasto', 'stanowisko', 'opis', 'wynagrodzenie', 'iloscMiejscMax',
            'iloscMiejscZajetych'
        ]

        widgets = {
            'id_Firma': forms.HiddenInput(),
            'iloscMiejscZajetych': forms.HiddenInput(),
        }


class DodajStudenta(forms.ModelForm):
    class Meta:
        model = Grupa
        fields = [
            'id_Praktyki', 'uczestnik'
        ]

        widgets = {
            'id_Praktyki': forms.HiddenInput(),
            'uczestnik': forms.HiddenInput(),
        }
