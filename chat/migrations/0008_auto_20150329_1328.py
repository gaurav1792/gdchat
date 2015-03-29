# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20150329_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_status',
            name='last_active',
        ),
        migrations.AddField(
            model_name='login_status',
            name='is_online',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='to_user',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
