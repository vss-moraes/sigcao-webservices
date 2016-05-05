from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from webservices import views


urlpatterns = [
    url(r'^ocorrencias/$', views.FiltraOcorrencias.as_view()),
    url(r'^ocorrencias/(?P<pk>[0-9]+)/$', views.DetalheOcorrencia.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
