# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-22 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0057_nurasymoaktoirasas_max_kiekis'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurasymoaktoirasas',
            name='PVM_iraso_pk',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
