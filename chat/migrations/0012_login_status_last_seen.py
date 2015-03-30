# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20150329_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_status',
            name='last_seen',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 3, 30, 18, 5, 36, 755255, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
