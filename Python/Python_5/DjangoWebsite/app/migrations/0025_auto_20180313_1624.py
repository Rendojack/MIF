# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_delete_nurasymoaktas'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KomisijosNarys',
        ),
        migrations.DeleteModel(
            name='NurasymoAktoIrasas',
        ),
    ]
