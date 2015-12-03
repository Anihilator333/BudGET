# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waluta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('waluta', models.CharField(max_length=10)),
                ('przelicznik', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='dochod',
            name='waluta',
            field=models.CharField(max_length=10, default='zł'),
        ),
        migrations.AddField(
            model_name='wydatek',
            name='waluta',
            field=models.CharField(max_length=10, default='zł'),
        ),
    ]
