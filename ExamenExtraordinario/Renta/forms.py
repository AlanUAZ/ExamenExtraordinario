# coding: utf-8
from django import forms
from Renta.models import Renta

class RentaForm(forms.ModelForm):
	"""Formulario para dar servicio al modelo Renta"""

	class Meta(object):
		model = Renta
		fields = ['fecha', 'cliente']