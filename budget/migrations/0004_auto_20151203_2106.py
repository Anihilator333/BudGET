# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20151203_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waluta',
            name='przelicznik',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
