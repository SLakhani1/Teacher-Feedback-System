# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-19 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SabKuch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrollment_id',
        ),
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]