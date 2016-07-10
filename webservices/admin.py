from django.contrib import admin
from .models import Ocorrencia, Sexo, Veterinario

# Register your models here.

admin.site.register(Ocorrencia)
admin.site.register(Sexo)
admin.site.register(Veterinario)
