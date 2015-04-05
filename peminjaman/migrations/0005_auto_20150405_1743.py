# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0004_pengawas'),
    ]

    operations = [
        migrations.CreateModel(
            name='mahasiswa',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=30)),
                ('npm', models.CharField(default=0, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='manager_ruangan',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=30)),
                ('nama', models.CharField(max_length=30)),
                ('nip', models.CharField(default=0, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='pengawas',
            name='nip',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='pengawas',
            name='role',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
