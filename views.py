from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def main_page(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'registration/login.html')


@login_required()
def account_user(request):
    return render(request, 'profile.html')


def signup_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(main_page)
        else:
            form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


