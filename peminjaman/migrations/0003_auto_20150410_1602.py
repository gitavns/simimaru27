# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0002_auto_20150410_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approval',
            old_name='izin_id',
            new_name='peminjaman_id',
        ),
        migrations.RenameField(
            model_name='komentar',
            old_name='pesan',
            new_name='komen',
        ),
    ]
