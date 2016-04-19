from .models import Endereco
from rest_framework import serializers


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'latitude', 'longitude')
