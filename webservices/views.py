from webservices.models import Ocorrencia, Veterinario
from webservices.serializers import OcorrenciaSerializer, EnvioOcorrenciaSerializer, VeterinarioSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

import json
import urllib3
import lxml.html

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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


def buscaCRMV(request):

    crmv = request.GET.get('crmv')
    try:
        veterinario = Veterinario.objects.get(crmv=crmv)
    except Veterinario.DoesNotExist:
        url = 'http://186.215.80.197/consulta/index.php?nome_regra=inicia&inscricao_uf=MS&inscricao_nro={0}&inscricao_classe=VP&uf=MS&flag=1'.format(crmv)
        xpath = '//*[@id="resultado"]/table//strong/text()'
        http = urllib3.PoolManager()
        resposta = http.request('GET', url)
        documento = lxml.html.document_fromstring(resposta.data)

        try:
            resultados = documento.xpath(xpath)
            veterinario = Veterinario(nome=resultados[1], estado=resultados[2], tipo_inscricao=resultados[3], situacao=resultados[4], crmv=crmv)
            print(veterinario.nome + veterinario.estado + veterinario.tipo_inscricao + veterinario.situacao + veterinario.crmv)
            if (veterinario.situacao.strip() == 'Atuante'):
                veterinario.save()
                serializer = VeterinarioSerializer(veterinario)
                return JSONResponse(serializer.data, status=201)
            print (veterinario.situacao + 'Não atuante')
            return HttpResponse(status=404)

        except Exception:
            print ('Erro no Scrapper')
            return HttpResponse(status=404)

    if (request.method == 'GET'):
        serializer = VeterinarioSerializer(veterinario)
        return JSONResponse(serializer.data)
    print('Deu merda')
    return HttpResponse(status=404)
