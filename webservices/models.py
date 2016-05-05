from django.db import models
# from django.utils import timezone


class Endereco(models.Model):
    endereco_completo = models.CharField(max_length=200, default="")
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=10)
    estado = models.CharField(max_length=2, default='MS')

    def __str__(self):
        return self.endereco_completo + '. ' + self.bairro + ', ' + self.cidade + ', ' + self.estado + '.'


class Doencas(models.Model):
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
    FAIXAS_ETARIAS = (
        ('Filhote', 'Filhote'),
        ('Jovem', 'Jovem'),
        ('Adulto', 'Adulto'),
        ('Idoso', 'Idoso'))

    nome = models.CharField(max_length=8, choices=FAIXAS_ETARIAS)

    def __str__(self):
        return self.nome


class Raca(models.Model):
    nome = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nome


class Ocorrencia(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    doenca = models.ForeignKey(Doencas, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    faixa_etaria = models.ForeignKey(FaixaEtaria, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    data = models.DateField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
