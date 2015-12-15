from django.conf.urls import url
from Renta.views import listar

urlpatterns = [
    url(r'^$', listar, name="lista"),
]