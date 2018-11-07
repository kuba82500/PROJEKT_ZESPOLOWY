from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def main_page(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'registration/login.html')


@login_required()
def account_user(request):
    return render(request, 'profile.html')


