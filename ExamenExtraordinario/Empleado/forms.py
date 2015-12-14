# coding: utf-8
from django import forms
from Empleado.models import Empleado

class EmpleadoForm(forms.models.Model):
	"""Formulario para dar servicio al modelo Empleado"""

	class Meta(object):
		model = Empleado
		fields = ['user', 'rfc']