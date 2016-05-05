from webservices.models import Ocorrencia
from webservices.serializers import OcorrenciaSeralizer
from rest_framework import generics


class DetalheOcorrencia(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSeralizer


class FiltraOcorrencias(generics.ListAPIView):
    serializer_class = OcorrenciaSeralizer

    def get_queryset(self):
        queryset = Ocorrencia.objects.all()
        doenca = self.request.query_params.get('doenca', None)
        faixa_etaria = self.request.query_params.get('faixa_etaria', None)
        sexo = self.request.query_params.get('sexo', None)
        raca = self.request.query_params.get('raca', None)

        if doenca is not None:
            queryset = queryset.filter(doenca__nome=doenca)
        if faixa_etaria is not None:
            queryset = queryset.filter(faixa_etaria__nome=faixa_etaria)
        if sexo is not None:
            queryset = queryset.filter(sexo__nome=sexo)
        if raca is not None:
            queryset = queryset.filter(raca__nome=raca)

        return queryset
