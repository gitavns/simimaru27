# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0002_ruangan_kapasitas'),
    ]

    operations = [
        migrations.AddField(
            model_name='komentar',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 5, 10, 18, 21, 691000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='approval_manager_ruangan',
            field=models.BooleanField(default=datetime.datetime(2015, 4, 5, 10, 18, 27, 689000, tzinfo=utc)),
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
            field=models.DateField(default=datetime.datetime(2015, 4, 5, 10, 18, 55, 733000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='waktu_mulai',
            field=models.TimeField(default=datetime.datetime(2015, 4, 5, 10, 19, 8, 309000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='waktu_selesai',
            field=models.TimeField(default=datetime.datetime(2015, 4, 5, 10, 19, 13, 286000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
