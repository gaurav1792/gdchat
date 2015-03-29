# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_remove_message_msg_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='from_user',
            new_name='lfrom_user',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='msg',
            new_name='lmsg',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='to_user',
            new_name='lto_user',
        ),
    ]
