# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0011_pesan'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesan',
            name='penerima_username',
            field=models.ForeignKey(related_name='pengirim_username', default=0, to='peminjaman.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pesan',
            name='pengirim_username',
            field=models.ForeignKey(related_name='penerima_username', to='peminjaman.user'),
        ),
    ]
