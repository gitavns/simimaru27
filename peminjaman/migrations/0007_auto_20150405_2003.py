# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0006_auto_20150405_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentar',
            name='user_komentar',
            field=models.ForeignKey(default=0, to='peminjaman.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='peminjam_username',
            field=models.ForeignKey(default=0, to='peminjaman.peminjam'),
            preserve_default=False,
        ),
    ]
