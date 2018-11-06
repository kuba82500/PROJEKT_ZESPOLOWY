from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'main.html')


def account_user(request):
    return render(request, 'account.html')
