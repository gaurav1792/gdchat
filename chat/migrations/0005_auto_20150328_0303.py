# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20150328_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_status',
            name='user',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
