# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20150328_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_status',
            name='is_online',
        ),
        migrations.AddField(
            model_name='login_status',
            name='last_active',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='msg_type',
            field=models.CharField(max_length=10, default='text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='to_user',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
