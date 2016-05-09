from webservices.models import Ocorrencia
from webservices.serializers import OcorrenciaSerializer
from rest_framework import generics
from itertools import chain


class FiltraOcorrencias(generics.ListAPIView):
    serializer_class = OcorrenciaSerializer

    def get_queryset(self):
        queryset = Ocorrencia.objects.all()

        sexo = self.request.query_params.get('sexo', None)
        faixas_etarias = self.request.query_params.getlist('faixa_etaria')
        racas = self.request.query_params.getlist('raca')
        doencas = self.request.query_params.getlist('doenca')

        if sexo is not None:
            queryset = list(queryset.filter(sexo__nome=sexo))
        if len(doencas) > 0:
            queryset = [item for item in queryset if str(item.doenca) in doencas]
        if len(faixas_etarias) > 0:
            queryset = [item for item in queryset if str(item.faixa_etaria) in faixas_etarias]
        if len(racas) > 0:
            queryset = [item for item in queryset if str(item.raca) in racas]

        return queryset


class EnviaOcorrencia(generics.CreateAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
