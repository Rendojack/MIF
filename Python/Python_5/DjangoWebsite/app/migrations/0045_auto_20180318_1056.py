# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 08:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0044_auto_20180318_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vardas', models.CharField(default=None, max_length=100)),
                ('pavarde', models.CharField(default=None, max_length=100)),
                ('pareigos', models.CharField(choices=[('ATSAKINGAS_ASMUO', 'Atsakingas asmuo'), ('KOMISIJOS NARYS PIRMININKAS', 'Komisijos narys pirmininkas'), ('KOMISIJOS NARYS', 'Komisijos narys'), ('DIREKTORIUS', 'Direktorius')], default=None, max_length=100)),
                ('darbo_istaiga', models.CharField(default=None, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='KomisijosNarys',
        ),
        migrations.AddField(
            model_name='nurasymoaktas',
            name='atsakingas_asmuo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atsakingas_asmuo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nurasymoaktas',
            name='patvirtines_direktorius',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patvirtines_direktorius', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nurasymoaktoirasas',
            name='israses_komisijos_narys',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
