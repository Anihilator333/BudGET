# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_auto_20151119_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dochod',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('użytkownik', models.CharField(max_length=50)),
                ('kategoria', models.CharField(max_length=50)),
                ('kwota', models.IntegerField(default=0)),
                ('dodane', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Income',
        ),
    ]
