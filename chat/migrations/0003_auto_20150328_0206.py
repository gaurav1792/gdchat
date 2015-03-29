# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20150328_0203'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='Login_status',
        ),
    ]
