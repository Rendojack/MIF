# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 14:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20180313_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurasymoaktoirasas',
            name='nurasymo_aktas',
        ),
    ]
