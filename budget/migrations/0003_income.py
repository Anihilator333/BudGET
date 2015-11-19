# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0002_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('kategoria', models.CharField(max_length=50)),
                ('kwota', models.IntegerField(default=0)),
                ('dodane', models.DateTimeField(auto_now_add=True)),
                ('użytkownik', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
