# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-22 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='image',
        ),
    ]
