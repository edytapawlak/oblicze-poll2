# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-14 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_status', models.BooleanField(default=False)),
            ],
        ),
    ]
