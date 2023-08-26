from django.db import models

class PK_Przyjecia(models.Model):
    class Meta:
        app_label = 'FormularzApp'  # Nazwa twojej aplikacji
    Data = models.DateField()
    Nr_tygodnia = models.IntegerField()
    Nr_rejestracyjne = models.CharField(max_length=50)
    Nr_plomby = models.CharField(max_length=50)
    Dane_kierowcy = models.CharField(max_length=100)
    Data_i_godzina_wjazdu = models.DateTimeField()
    Data_i_godzina_podstawienia = models.DateTimeField()
    Data_i_godzina_wyjazdu = models.DateTimeField()
    Ilość_palet = models.IntegerField()
    Ilość_kartonów = models.IntegerField()
    Ilość_sztuk = models.IntegerField()
    Osoby_na_rozładunku = models.IntegerField()
    Dostawca = models.CharField(max_length=100)
    Nr_dostaw = models.CharField(max_length=50)
    Luzem_Palety_Mieszane = models.CharField(max_length=10, choices=[
        ('Luzem', 'Luzem'),
        ('Palety', 'Palety'),
        ('Mieszane', 'Mieszane')
    ])
    Data_przyjecia_na_PTO = models.DateField()

    def __str__(self):
        return self.Nr_rejestracyjne

