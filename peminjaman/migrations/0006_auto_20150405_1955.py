# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0005_auto_20150405_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='mahasiswa',
        ),
        migrations.DeleteModel(
            name='manager_ruangan',
        ),
        migrations.DeleteModel(
            name='pengawas',
        ),
        migrations.AlterField(
            model_name='peminjaman',
            name='jumlah_peserta',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='peminjam',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to='peminjaman.user')),
            ],
        ),
    ]
