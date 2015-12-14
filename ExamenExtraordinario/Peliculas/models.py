# -*- encoding: utf-8 -*-
from django.db import models
from Genero.models import Genero

# Create your models here.

class Peliculas(models.Model):
	clave = models.CharField(max_length=10)
	titulo = models.CharField(max_length=15)
	duracion = models.CharField(max_length=10)
	sinopsis = models.CharField(max_length=25)
	clasificacion = models.CharField(max_length=5)
	genero = models.ForeignKey(Genero)

	def __unicode__(self):
		return self.titulo + " " + self.genero