# -*- encoding: utf-8 -*-
from django.db import models
from Cliente.models import Cliente

# Create your models here.

class Renta(models.Model):
	fecha = models.DateField('Fecha de renta')
	cliente =  models.ForeignKey(Cliente)

	def __unicode__(self):
		return self.fecha + " " + self.cliente