# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20170619_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='entry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]