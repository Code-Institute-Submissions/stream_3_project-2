# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default='', max_length=40),
        ),
    ]
