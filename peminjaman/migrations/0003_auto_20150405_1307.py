# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0002_ruangan_kapasitas'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentar',
            name='timestamp',
            field=models.DateTimeField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='approval_manager_ruangan',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='jumlah_peserta',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='tanggal',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='waktu_mulai',
            field=models.TimeField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='waktu_selesai',
            field=models.TimeField(default=0),
            preserve_default=False,
        ),
    ]
