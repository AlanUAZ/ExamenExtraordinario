# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renta', '0001_initial'),
        ('Peliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleRenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaentrega', models.CharField(max_length=10)),
                ('pelicula', models.ForeignKey(to='Peliculas.Peliculas')),
                ('renta', models.ForeignKey(to='Renta.Renta')),
            ],
        ),
    ]
