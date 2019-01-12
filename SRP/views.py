from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StworzPraktyke
from .models import Praktyki
from accounts.models import User


def main_page(request):
    return render(request, 'main.html')


@login_required()
def user_profile(request):
    return render(request, 'account/profile.html')


def lista_praktyk(request):
    listapraktyk = Praktyki.objects.all()
    return render(request, 'practice/praktyki.html', {'listapraktyk': listapraktyk})


def stworz_Praktyke(request):
    user = User.objects.get(nazwafirmy=request.user.nazwafirmy)

    form = StworzPraktyke(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.id_Firma = user
        instance.save()
        redirect(lista_praktyk)

    return render(request, 'practice/stworz_Praktyke.html', {'form': form}, {'user',user})


def edytuj_praktyke(request, id_Praktyki):
    praktyka = get_object_or_404(Praktyki, pk=id_Praktyki)
    form_praktyk = StworzPraktyke(request.POST or None, instance=praktyka)

    if form_praktyk.is_valid():
        form_praktyk.save()

    return render(request, 'practice/stworz_Praktyke.html', {'form_praktyk': form_praktyk})


def usun_praktyke(request, id_Praktyki):
    praktyka = get_object_or_404(Praktyki, pk=id_Praktyki)

    if request.method == 'POST':
        praktyka.delete()
        return redirect(lista_praktyk)

    return render(request, 'practice/confirm.html', {'praktyka': praktyka})


def CRUD(request):
    return render(request, 'practice/CRUD.html')
