# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180310_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvmirasas',
            name='PVM_suma',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='PVM_tarifas',
            field=models.FloatField(default=21),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='kiekis',
            field=models.FloatField(default=8),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='suma_be_PVM',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='suma_viso',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='vnt_kaina_be_PVM',
            field=models.FloatField(default=5),
        ),
    ]
