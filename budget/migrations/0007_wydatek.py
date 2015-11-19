# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0006_auto_20151119_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wydatek',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('użytkownik', models.CharField(max_length=50)),
                ('kategoria', models.CharField(max_length=50)),
                ('kwota', models.IntegerField(default=0)),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
