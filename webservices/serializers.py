from .models import Endereco, Ocorrencia
from rest_framework import serializers


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'endereco_completo', 'bairro', 'cidade', 'estado')


class OcorrenciaSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ('id', 'endereco', 'doenca', 'sexo', 'faixa_etaria', 'raca', 'data', 'latitude', 'longitude')
