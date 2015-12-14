# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Genero(models.Model):
	genero = models.CharField(max_length=15)

	def __unicode__(self):
		return self.genero