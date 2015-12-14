# coding: utf-8
from django import forms
from Genero.models import Genero

class GeneroForm(forms.models.Model):
	"""Formulario para dar servicio al modelo Genero"""

	class Meta(object):
		model = Genero
		fields = ['genero']
