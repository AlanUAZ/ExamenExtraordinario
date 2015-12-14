# coding: utf-8
from django import forms
from DetalleRenta.models import DetalleRenta

class DetalleRentaForm(forms.models.Model):
	"""Formulario para dar servicio al modelo DetalleRenta"""

	class Meta(object):
		model = DetalleRenta
		fields = ['pelicula', 'fechaentrega', 'renta']