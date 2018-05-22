# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180310_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvmirasas',
            name='PVM_tarifas',
            field=models.DecimalField(decimal_places=2, default=21, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='kiekis',
            field=models.DecimalField(decimal_places=2, default=8, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='matavimo_vnt',
            field=models.CharField(default='vnt', max_length=100),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='prekes_pavadinimas',
            field=models.CharField(default='bananas', max_length=100),
        ),
        migrations.AlterField(
            model_name='pvmirasas',
            name='vnt_kaina_be_PVM',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=8),
        ),
    ]