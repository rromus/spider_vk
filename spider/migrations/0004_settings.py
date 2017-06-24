# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0003_auto_20170621_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filters', models.TextField()),
                ('urls', models.TextField()),
                ('runs', models.BooleanField(default=False)),
                ('run_last_time', models.DateTimeField()),
                ('run_delay', models.IntegerField(default=5)),
                ('status', models.CharField(default='Idle', max_length=50)),
            ],
        ),
    ]
