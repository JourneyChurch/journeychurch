# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20170519_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='link',
            new_name='link_url',
        ),
    ]