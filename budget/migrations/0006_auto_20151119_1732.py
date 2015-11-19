# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20151119_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dochod',
            old_name='dodane',
            new_name='data_dodania',
        ),
    ]
