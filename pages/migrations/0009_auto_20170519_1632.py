# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20170519_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='navigation',
            new_name='menu',
        ),
    ]