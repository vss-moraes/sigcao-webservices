from webservices.models import Ocorrencia
from webservices.serializers import OcorrenciaSerializer, EnvioOcorrenciaSerializer
from rest_framework import generics
import json


class FiltraOcorrencias(generics.ListAPIView):
    serializer_class = OcorrenciaSerializer

    def termos_da_busca(self, nome_do_campo, nome_arquivo):
        parametros_request = self.request.query_params.getlist(nome_do_campo)
        if len(parametros_request) > 0:
            return parametros_request

        with open(nome_arquivo, 'r') as arquivo:
            lista = json.load(arquivo)

        return [item['fields']['nome'] for item in lista]

    def get_queryset(self):
        racas = self.termos_da_busca('raca', 'fixtures/lista_racas.json')
        faixas_etarias = self.termos_da_busca('faixa_etaria', 'fixtures/lista_faixa_etaria.json')
        doencas = self.termos_da_busca('doenca', 'fixtures/lista_doencas.json')
        sexo = self.request.query_params.get('sexo', None)

        print (self.request.query_params)

        if self.request.query_params.get('doenca', None):
            queryset = Ocorrencia.objects.filter(raca__nome__in=racas).filter(doenca__nome__in=doencas).filter(faixa_etaria__nome__in=faixas_etarias)
        else:
            queryset = None

        if sexo is not None:
            queryset = queryset.filter(sexo__nome=sexo)

        return queryset


class EnviaOcorrencia(generics.ListCreateAPIView):
    serializer_class = EnvioOcorrenciaSerializer

    def get_queryset(self):
        return None
