# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20180313_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pvmsask',
            name='nurasymo_aktas',
        ),
        migrations.AddField(
            model_name='nurasymoaktas',
            name='PVM_saskaitos',
            field=models.ManyToManyField(default=None, to='app.PVMSask'),
        ),
    ]
