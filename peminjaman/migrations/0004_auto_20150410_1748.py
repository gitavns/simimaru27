# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peminjaman', '0003_auto_20150410_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='komen',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='peminjam',
            name='nama',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pengawas',
            name='nama',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pengawas',
            name='role',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
