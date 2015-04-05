# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0003_auto_20150405_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='pengawas',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
    ]
