from django.forms import ModelForm
from .models import Uzytkownik
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = Uzytkownik
        fields = ['imie', 'nazwisko', 'email', 'haslo', 'numerIndeksu']
