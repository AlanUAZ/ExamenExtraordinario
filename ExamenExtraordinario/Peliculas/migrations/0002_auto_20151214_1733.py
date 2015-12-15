# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='sinopsis',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
