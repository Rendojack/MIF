# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20180313_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvmsask',
            name='nurasymo_aktas',
        ),
    ]
