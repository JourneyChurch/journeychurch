# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]