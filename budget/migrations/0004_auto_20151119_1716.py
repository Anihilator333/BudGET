# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='użytkownik',
            field=models.CharField(max_length=50),
        ),
    ]
