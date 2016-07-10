from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from webservices import views


urlpatterns = [
    url(r'^ocorrencias/$', views.FiltraOcorrencias.as_view()),
    url(r'^ocorrencias/nova/$', views.EnviaOcorrencia.as_view()),
    url(r'^veterinario/busca/$', views.buscaCRMV),
]

urlpatterns = format_suffix_patterns(urlpatterns)
