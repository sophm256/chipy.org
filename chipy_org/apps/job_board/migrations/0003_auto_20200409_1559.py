# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-09 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0002_auto_20200409_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='approval_date',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending Approval'), ('approved', 'Approved'), ('denied', 'Denied'), ('extended', 'Extended'), ('archived', 'Archived')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='status_change_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
