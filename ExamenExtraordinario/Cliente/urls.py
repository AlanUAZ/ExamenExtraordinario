from django.conf.urls import include, url
from .views import listar

urlpatterns = [
    url(r'^$', listar, name="lista"),
]