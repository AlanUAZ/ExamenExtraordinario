# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(max_length=10)),
                ('titulo', models.CharField(max_length=15)),
                ('duracion', models.CharField(max_length=10)),
                ('sinopsis', models.CharField(max_length=25)),
                ('clasificacion', models.CharField(max_length=5)),
                ('genero', models.ForeignKey(to='Genero.Genero')),
            ],
        ),
    ]
