# -*- coding: utf-8 -*-
# Generated by Django 1.10b1 on 2016-07-23 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overtime', '0003_report_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='month',
        ),
        migrations.AddField(
            model_name='report',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
