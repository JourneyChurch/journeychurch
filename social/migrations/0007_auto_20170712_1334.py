# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20170623_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='entry_date',
            field=models.DateTimeField(null=True),
        ),
    ]
