# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renta',
            name='fecha',
            field=models.DateField(verbose_name=b'Fecha de renta'),
        ),
    ]
