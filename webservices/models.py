from django.db import models
from django.utils import timezone


class Doenca(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Sexo(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'))

    nome = models.CharField(max_length=1, choices=GENEROS)

    def __str__(self):
        return self.nome


class FaixaEtaria(models.Model):
    nome = models.CharField(max_length=8, default="")

    def __str__(self):
        return self.nome


class Raca(models.Model):
    nome = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nome


class Ocorrencia(models.Model):
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    faixa_etaria = models.ForeignKey(FaixaEtaria, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)

    data = models.DateField(default=timezone.now)
    endereco_completo = models.CharField(max_length=200, default="")
    bairro = models.CharField(max_length=50, default="")
    cidade = models.CharField(max_length=10, default="")
    estado = models.CharField(max_length=2, default='MS')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def __str__(self):
        return self.endereco_completo
