from django.db import models
# from django.utils import timezone


class Endereco(models.Model):
    logradouro = models.CharField(max_length=30)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length=2, default='MS')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.logradouro + ' ' + self.rua + ', numero ' + str(self.numero) + '. ' + self.bairro + ', ' + self.cidade + ', ' + self.estado + '.'
