# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20150329_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='lfrom_user',
            new_name='from_user',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='lmsg',
            new_name='msg',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='lto_user',
            new_name='to_user',
        ),
        migrations.AddField(
            model_name='message',
            name='msg_type',
            field=models.CharField(max_length=10, default='text'),
            preserve_default=True,
        ),
    ]
