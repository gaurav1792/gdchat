# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('is_online', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='follows',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_online',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
