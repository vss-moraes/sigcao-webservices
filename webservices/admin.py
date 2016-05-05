from django.contrib import admin
from .models import Endereco, Ocorrencia, Doencas, Sexo, FaixaEtaria, Raca

# Register your models here.

admin.site.register(Endereco)
admin.site.register(Ocorrencia)
admin.site.register(Doencas)
admin.site.register(Sexo)
admin.site.register(FaixaEtaria)
admin.site.register(Raca)
