from .models import Ocorrencia
from rest_framework import serializers


# class EnderecoSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Endereco
#        fields = ('endereco_completo', 'bairro', 'cidade', 'estado')


class EnvioOcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        depth = 1
