# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(blank=True, null=True, max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('udpated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
