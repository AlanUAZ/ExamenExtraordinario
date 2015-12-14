# -*- encoding: utf-8 -*-
from django.db import models
from Renta.models import Renta
from Peliculas.models import Peliculas

# Create your models here.

class DetalleRenta(models.Model):
	pelicula =  models.ForeignKey(Peliculas)
	fechaentrega = models.CharField(max_length=10)
	renta = models.ForeignKey(Renta)

	def __unicode__(self):
		return self.pelicula + " " + self.fechaentrega