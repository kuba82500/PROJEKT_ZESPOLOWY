from django.shortcuts import render, redirect
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


def praktyki(request):
    praktyka = Praktyki.objects.all()
    return render(request, 'praktyki.html', {'praktyki': praktyki})


def stworz_Praktyke(request):
    form_praktyk = StworzPraktyke(request.POST or None)

    if form_praktyk.is_valid():
        form_praktyk.save()

    return render(request, 'stworz_Praktyke.html', {'form_praktyk': form_praktyk})


def signup_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = RegisterForm.save()
            form.save()
            return redirect(main_page)
        else:
            form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})