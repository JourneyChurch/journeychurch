# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-11 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_auto_20170623_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='date',
        ),
    ]