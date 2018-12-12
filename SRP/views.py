from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, StworzPraktyke
from .models import Praktyki


def main_page(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'registration/login.html')


@login_required()
def account_user(request):
    return render(request, 'profile.html')


def lista_praktyk(request):
    listapraktyk = Praktyki.objects.all()
    return render(request, 'praktyki.html', {'listapraktyk': listapraktyk})


def stworz_Praktyke(request):
    form_praktyk = StworzPraktyke(request.POST or None)

    if form_praktyk.is_valid():
        form_praktyk.save()

    return render(request, 'stworz_Praktyke.html', {'form_praktyk': form_praktyk})


def edytuj_praktyke(request, id_Praktyki):
    praktyka = get_object_or_404(Praktyki, pk=id_Praktyki)
    form_praktyk = StworzPraktyke(request.POST or None, instance=praktyka)

    if form_praktyk.is_valid():
        form_praktyk.save()

    return render(request, 'stworz_Praktyke.html', {'form_praktyk': form_praktyk})


def usun_praktyke(request, id_Praktyki):
    praktyka = get_object_or_404(Praktyki, pk=id_Praktyki)

    if request.method == 'POST':
        praktyka.delete()
        return redirect(lista_praktyk)

    return render(request, 'confirm.html', {'praktyka': praktyka})


def CRUD(request):
    return render(request, 'CRUD.html')


def signup_view(request):
    form_register = RegisterForm
    if request.method == 'POST':
        form_register = RegisterForm(request.POST)
        if form_register.is_valid():
            form_register = RegisterForm.save()
            form_register.save()
            return redirect(main_page)
        else:
            form_register = RegisterForm()
    return render(request, 'registration/signup.html', {'form_register': form_register})
