from django.conf.urls import include, url
from .views import listar, login_view

urlpatterns = [
    url(r'^$', listar, name="lista"),
    url(r'^login$', login_view, name="login_view"),
]