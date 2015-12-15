from django.conf.urls import url
from DetalleRenta.views import listar

urlpatterns = [
    url(r'^$', listar, name="lista_detalle"),
]