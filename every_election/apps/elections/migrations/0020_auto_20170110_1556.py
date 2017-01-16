# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-10 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0019_auto_20170110_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='electedrole',
            name='elected_role_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='election',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='elections.Election'),
        ),
    ]
