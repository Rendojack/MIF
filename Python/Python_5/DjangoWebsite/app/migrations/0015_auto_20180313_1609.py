# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20180313_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvmsask',
            name='nurasymo_aktas',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.NurasymoAktas'),
        ),
    ]
