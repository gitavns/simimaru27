# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='komentar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pesan', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='peminjaman',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=50)),
                ('no_telp', models.CharField(max_length=13)),
                ('nama_kegiatan', models.CharField(max_length=50)),
                ('deskripsi', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='ruangan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gedung', models.CharField(max_length=1)),
                ('lantai', models.CharField(max_length=1)),
                ('nomor', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='ruangan_id',
            field=models.ForeignKey(to='peminjaman.ruangan'),
        ),
        migrations.AddField(
            model_name='komentar',
            name='izin_id',
            field=models.ForeignKey(to='peminjaman.peminjaman'),
        ),
    ]
