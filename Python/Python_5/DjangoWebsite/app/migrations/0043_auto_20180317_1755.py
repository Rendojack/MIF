# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_nurasymoaktas_is_submited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvmirasas',
            name='nurasymo_aktas',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.NurasymoAktas'),
        ),
    ]