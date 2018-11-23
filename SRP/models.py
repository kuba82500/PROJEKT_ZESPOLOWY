from django.db import models


class Firma(models.Model):
    id_firma = models.AutoField(primary_key=True, default=1)
    nazwaFirmy = models.CharField(max_length=45, name="NazwaFirmy")
    haslo = models.CharField(max_length=32, name="haslo")
    email = models.EmailField()
    czyZaakceptowano = models.BooleanField()


class Praktyki(models.Model):
    id_Praktyki = models.AutoField(primary_key=True, default=1)
    iloscMiejscMax = models.IntegerField(name="iloscMiejscMax")
    iloscMiejscZajetych = models.IntegerField(name="iloscMiejscZajetych")
    dataUtworzenia = models.DateTimeField(name="DataUtworzenia")

    dataRozpoczecia = models.DateTimeField(name="DataRozpoczecia")
    dataZakonczenia = models.DateTimeField(name="DataZakonczenia")
    czyPlatne = models.BooleanField()
    wynagrodzenia = models.CharField(max_length=45, name="wynagrodzenie")
    stanowisko = models.CharField(max_length=45, name="Stanowisko")
    opis = models.TextField(max_length=255, name="opis")
    miasto = models.CharField(max_length=45, name="miasto")
    #id_Firma = models.ForeignKey(Firma, on_delete=models.SET_NULL())


class Grupa(models.Model):
    id_Grupy = models.AutoField(primary_key=True, default=1)
    imieUczestnika = models.CharField(max_length=45, name="imieUczestnika")
    nazwiskoUczestnika = models.CharField(max_length=45, name="nazwiskoUczestnika")
    imieProwadzacego = models.CharField(max_length=45, name="imieProwadzacego")
    nazwiskoProwadzacego = models.CharField(max_length=45, name="nazwiskoProwadzacego")
    #id_Praktyki = models.ForeignKey(Praktyki, on_delete=models.CASCADE)
    #id_Firma = models.ForeignKey(Firma, on_delete=models.CASCADE)


class Uzytkownik(models.Model):
    id_Uzytkownika = models.AutoField(primary_key=True, default=1)
    imie = models.CharField(max_length=45, name="imie")
    nazwisko = models.CharField(max_length=45, name="nazwisko")
    email = models.EmailField()
    haslo = models.CharField(max_length=45, name="haslo")
    nrIndex = models.CharField(max_length=45, name="numerIndeksu")
    #dataUtworzenia = models.DateTimeField()
    #dataEdycji = models.DateTimeField()
    #czyAdmin = models.BooleanField()
    #id_Grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE)
    #id_Praktyki = models.ForeignKey(Praktyki, on_delete=models.CASCADE)
    #id_Firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
