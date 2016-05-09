from .models import Ocorrencia
from rest_framework import serializers


# class EnderecoSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Endereco
#        fields = ('endereco_completo', 'bairro', 'cidade', 'estado')


class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = (
            'id',
            'doenca',
            'sexo',
            'faixa_etaria',
            'raca',
            'data',
            'endereco_completo',
            'bairro',
            'cidade',
            'estado',
            'latitude',
            'longitude')
        depth = 1
