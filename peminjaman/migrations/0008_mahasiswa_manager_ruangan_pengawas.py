# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0007_auto_20150405_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='mahasiswa',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to='peminjaman.peminjam')),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=30)),
                ('npm', models.CharField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='manager_ruangan',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to='peminjaman.peminjam')),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=30)),
                ('nip', models.CharField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='pengawas',
            fields=[
                ('username', models.ForeignKey(primary_key=True, serialize=False, to='peminjaman.user')),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
                ('nip', models.CharField(default=0, max_length=10)),
            ],
        ),
    ]
