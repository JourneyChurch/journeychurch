# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20170612_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='entry_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='videogroup',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='videogroup',
            name='entry_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='videogroup',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='videogroup',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='videogroup',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='videogroup',
            name='title',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
