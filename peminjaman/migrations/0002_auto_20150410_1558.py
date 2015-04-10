# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='komentar',
            old_name='izin_id',
            new_name='peminjaman_id',
        ),
    ]
