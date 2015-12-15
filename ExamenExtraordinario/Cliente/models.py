# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cliente(models.Model):
    user = models.OneToOneField(User)
    domicilio = models.CharField(max_length=40)
    rfc = models.CharField(max_length=13)
    telofono = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user.first_name+" "+self.user.last_name
