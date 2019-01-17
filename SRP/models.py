from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import datetime


class Praktyki(models.Model):
    id_Praktyki = models.AutoField(primary_key=True)
    iloscMiejscMax = models.CharField(null=True, blank=True, max_length=15)
    iloscMiejscZajetych = models.CharField(blank=True, null=True, max_length=15, default=0)
    dataUtworzenia = models.DateField(auto_now_add=True)
    dataRozpoczecia = models.DateField(null=True, blank=True)
    dataZakonczenia = models.DateField(null=True, blank=True)
    wynagrodzenie = models.CharField(max_length=45, blank=True, null=True)
    stanowisko = models.CharField(max_length=45)
    opis = models.TextField(max_length=255, blank=True, null=True)
    miasto = models.CharField(max_length=45, blank=True, null=True)
    id_Firma = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.stanowisko


class Grupa(models.Model):
    id_Grupy = models.AutoField(primary_key=True)
    id_Praktyki = models.ForeignKey(Praktyki, on_delete=models.CASCADE, blank=True, null=True)
    uczestnik = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True,
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return self.id_Praktyki.stanowisko
