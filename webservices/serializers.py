from .models import Ocorrencia, Veterinario
from rest_framework import serializers


class EnvioOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        depth = 1

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
