# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20180313_1703'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KomisijosNarys',
        ),
        migrations.RemoveField(
            model_name='nurasymoaktoirasas',
            name='nurasymo_aktas',
        ),
        migrations.DeleteModel(
            name='NurasymoAktas',
        ),
        migrations.DeleteModel(
            name='NurasymoAktoIrasas',
        ),
    ]
