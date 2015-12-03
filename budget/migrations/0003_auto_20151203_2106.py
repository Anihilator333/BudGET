# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20151203_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waluta',
            name='przelicznik',
            field=models.DecimalField(max_digits=10, decimal_places=6),
        ),
    ]
