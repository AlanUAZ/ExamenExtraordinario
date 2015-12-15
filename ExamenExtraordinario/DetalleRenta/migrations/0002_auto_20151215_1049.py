# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DetalleRenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallerenta',
            name='fechaentrega',
            field=models.DateField(verbose_name=b'Fecha de entrega'),
        ),
    ]
