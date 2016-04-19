from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from webservices import views


urlpatterns = [
    url(r'^enderecos/$', views.ListaEndereco.as_view()),
    url(r'^enderecos/(?P<pk>[0-9]+)/$', views.DetalheEndereco.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
