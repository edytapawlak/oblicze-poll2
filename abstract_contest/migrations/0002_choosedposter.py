# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-04 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20171130_2152'),
        ('abstract_contest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoosedPoster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Poster')),
            ],
        ),
    ]
