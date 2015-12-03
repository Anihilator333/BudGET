# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dochod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('użytkownik', models.CharField(max_length=50)),
                ('kategoria', models.CharField(max_length=50)),
                ('kwota', models.DecimalField(decimal_places=2, max_digits=6, default=0)),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=150, blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('udpated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wydatek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('użytkownik', models.CharField(max_length=50)),
                ('kategoria', models.CharField(max_length=50)),
                ('kwota', models.DecimalField(decimal_places=2, max_digits=6, default=0)),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
