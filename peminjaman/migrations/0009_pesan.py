# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0008_mahasiswa_manager_ruangan_pengawas'),
    ]

    operations = [
        migrations.CreateModel(
            name='pesan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pesan', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
