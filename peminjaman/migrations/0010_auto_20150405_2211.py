# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0009_pesan'),
    ]

    operations = [
        migrations.CreateModel(
            name='approval_pengawas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approval', models.BooleanField()),
                ('izin_id', models.ForeignKey(to='peminjaman.peminjaman')),
                ('pengawas_username', models.ForeignKey(to='peminjaman.pengawas')),
            ],
        ),
        migrations.DeleteModel(
            name='pesan',
        ),
    ]
