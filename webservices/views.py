from webservices.models import Endereco
from webservices.serializers import EnderecoSerializer
from rest_framework import generics


class ListaEndereco(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class DetalheEndereco(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
