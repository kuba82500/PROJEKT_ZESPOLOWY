from django.db import models


class Firma(models.Model):
    id_firma = models.AutoField(primary_key=True)
    nazwaFirmy = models.CharField(max_length=45, name="NazwaFirmy")
    haslo = models.CharField(max_length=32, name="haslo")
    email = models.EmailField()
    czyZaakceptowano = models.BooleanField()


class Praktyki(models.Model):
    id_Praktyki = models.AutoField(primary_key=True)
    iloscMiejscMax = models.IntegerField(name="iloscMiejscMax")
    iloscMiejscZajetych = models.IntegerField(name="iloscMiejscZajetych", blank=True)
    dataUtworzenia = models.DateField(name="DataUtworzenia", blank=True)
    dataRozpoczecia = models.DateField(name="DataRozpoczecia", blank=True)
    dataZakonczenia = models.DateField(name="DataZakonczenia", blank=True)
    czyPlatne = models.BooleanField(blank=True)
    wynagrodzenie = models.CharField(max_length=45, name="wynagrodzenie", blank=True)
    stanowisko = models.CharField(max_length=45, name="stanowisko")
    opis = models.TextField(max_length=255, name="opis")
    miasto = models.CharField(max_length=45, name="miasto")
    id_Firma = models.ForeignKey(Firma, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.stanowisko


class Grupa(models.Model):
    id_Grupy = models.AutoField(primary_key=True)
    imieUczestnika = models.CharField(max_length=45, name="imieUczestnika")
    nazwiskoUczestnika = models.CharField(max_length=45, name="nazwiskoUczestnika")
    imieProwadzacego = models.CharField(max_length=45, name="imieProwadzacego")
    nazwiskoProwadzacego = models.CharField(max_length=45, name="nazwiskoProwadzacego")
    id_Praktyki = models.ForeignKey(Praktyki, on_delete=models.CASCADE)
    id_Firma = models.ForeignKey(Firma, on_delete=models.CASCADE)


class Uzytkownik(models.Model):
    id_Uzytkownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45, name="imie")
    nazwisko = models.CharField(max_length=45, name="nazwisko")
    email = models.EmailField()
    haslo = models.CharField(max_length=45, name="haslo")
    nrIndex = models.CharField(max_length=45, name="numerIndeksu", blank=True)
    dataUtworzenia = models.DateField()
    czyAdmin = models.BooleanField()
    id_Grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE, blank=True)
    id_Praktyki = models.ForeignKey(Praktyki, on_delete=models.CASCADE, blank=True)
    id_Firma = models.ForeignKey(Firma, on_delete=models.CASCADE, blank=True)
