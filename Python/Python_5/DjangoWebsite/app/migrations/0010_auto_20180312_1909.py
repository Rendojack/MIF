# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180312_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pvmirasas',
            old_name='PVM_sask',
            new_name='PVM_saskaita',
        ),
    ]
