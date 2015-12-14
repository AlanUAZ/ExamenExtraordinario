# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empleado(models.Model):
	user = models.OneToOneField(User)
	rfc = models.CharField(max_length=13)

	def __unicode__(self):
		return self.user.first_name+" "+self.user.last_name