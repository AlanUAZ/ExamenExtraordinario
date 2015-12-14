# coding: utf-8
from django import forms
from Peliculas.models import Peliculas

class PeliculasForm(forms.ModelForm):
	"""Formulario para dar servicio al modelo Peliculas"""

	class Meta(object):
		model = Peliculas
		fields = ['clave', 'titulo', 'duracion', 'sinopsis', 'clasificacion', 'genero']
		