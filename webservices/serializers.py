from .models import Ocorrencia
from rest_framework import serializers


class EnvioOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        depth = 1
