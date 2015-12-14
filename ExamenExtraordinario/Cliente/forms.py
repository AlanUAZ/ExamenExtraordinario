# coding: utf-8
from django import forms
from Cliente.models import Cliente

class ClienteForm(forms.models.Model):
	"""Formulario para dar servicio al modelo Cliente"""

	class Meta(object):
		model = Cliente
		fields = ['user', 'domicilio', 'rfc', 'telefono']