from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StworzPraktyke, DodajStudenta, AktywujFirme
from .models import Praktyki, Grupa
from accounts.models import User


def main_page(request):
    return render(request, 'main.html')


@login_required()
def listafirm(request):
    firma = User.objects.all()
    return render(request, 'account/firmy.html', {'firmy': firma})


@login_required()
def activefirm(request, id):
    firma = get_object_or_404(User, id=id)
    form = AktywujFirme(request.POST or None, instance=firma)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'account/activefirm.html', {'form': form})


@login_required()
def user_profile(request):
    user = User.objects.get(email=request.user.email)
    praktyka = Grupa.objects.all().filter(uczestnik=user)
    return render(request, 'account/profile.html', {'praktyka': praktyka})


def lista_praktyk(request):
    lista_praktyk = Praktyki.objects.all()
    lista_grup = Grupa.objects.all()
    return render(request, 'practice/praktyki.html', {'listapraktyk': lista_praktyk}, {'lista_grup': lista_grup})


@login_required()
def lista_praktyk_firma(request):
    user = User.objects.get(nazwafirmy=request.user.nazwafirmy)
    listapraktyk = Praktyki.objects.all().filter(id_Firma=user)
    return render(request, 'practice/praktyki.html', {'listapraktyk': listapraktyk})


@login_required()
def stworz_Praktyke(request):
    user = User.objects.get(nazwafirmy=request.user.nazwafirmy)

    form = StworzPraktyke(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.id_Firma = user
        instance.save()
        return redirect(lista_praktyk_firma)

    return render(request, 'practice/stworz_Praktyke.html', {'form': form}, {'user': user})


@login_required()
def edytuj_praktyke(request, id_Praktyki):
    praktyka = get_object_or_404(Praktyki, pk=id_Praktyki)
    form = StworzPraktyke(request.POST or None, instance=praktyka)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'practice/edytuj_praktyke.html', {'form': form})


@login_required()
def usun_praktyke(request, id_Praktyki):
    praktyka = get_object_or_404(Praktyki, pk=id_Praktyki)

    if request.method == 'POST':
        praktyka.delete()
        return redirect(lista_praktyk_firma)

    return render(request, 'practice/confirm.html', {'praktyka': praktyka})


@login_required()
def dolaczdopraktyk(request, id_Praktyki):
    praktyka = get_object_or_404(Praktyki, pk=id_Praktyki)
    user = User.objects.get(email=request.user.email)
    form = DodajStudenta(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id_Praktyki = praktyka
            instance.uczestnik = user
            instance.save()
        return redirect(lista_praktyk)

    return render(request, 'practice/dolacz.html', {'form': form})
