# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20150328_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
