# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approval', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pesan', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tanggal', models.DateField()),
                ('waktu_mulai', models.TimeField()),
                ('waktu_selesai', models.TimeField()),
                ('email', models.CharField(max_length=50)),
                ('no_telp', models.CharField(max_length=13)),
                ('nama_kegiatan', models.CharField(max_length=50)),
                ('deskripsi', models.CharField(max_length=350)),
                ('jumlah_peserta', models.IntegerField(default=0)),
                ('approval_manager_ruangan', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pesan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pesan', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruangan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gedung', models.CharField(max_length=1)),
                ('lantai', models.CharField(max_length=1)),
                ('nomor', models.CharField(max_length=5)),
                ('kapasitas', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peminjam',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='peminjaman.User')),
                ('nama', models.CharField(max_length=30)),
            ],
            bases=('peminjaman.user',),
        ),
        migrations.CreateModel(
            name='Pengawas',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='peminjaman.User')),
                ('nama', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
                ('nip', models.CharField(default=0, max_length=10)),
            ],
            bases=('peminjaman.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='pesan',
            field=models.ManyToManyField(to='peminjaman.User', through='peminjaman.Pesan'),
        ),
        migrations.AddField(
            model_name='pesan',
            name='penerima_username',
            field=models.ForeignKey(related_name='pengirim_username', to='peminjaman.User'),
        ),
        migrations.AddField(
            model_name='pesan',
            name='pengirim_username',
            field=models.ForeignKey(related_name='penerima_username', to='peminjaman.User'),
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='ruangan_id',
            field=models.ForeignKey(to='peminjaman.Ruangan'),
        ),
        migrations.AddField(
            model_name='komentar',
            name='izin_id',
            field=models.ForeignKey(to='peminjaman.Peminjaman'),
        ),
        migrations.AddField(
            model_name='komentar',
            name='user_komentar',
            field=models.ForeignKey(to='peminjaman.User'),
        ),
        migrations.AddField(
            model_name='approval',
            name='izin_id',
            field=models.ForeignKey(to='peminjaman.Peminjaman'),
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('peminjam_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='peminjaman.Peminjam')),
                ('npm', models.CharField(default=0, max_length=10)),
            ],
            bases=('peminjaman.peminjam',),
        ),
        migrations.CreateModel(
            name='Manager_Ruangan',
            fields=[
                ('peminjam_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='peminjaman.Peminjam')),
                ('nip', models.CharField(default=0, max_length=10)),
            ],
            bases=('peminjaman.peminjam',),
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='approval_pengawas',
            field=models.ManyToManyField(to='peminjaman.Pengawas', through='peminjaman.Approval'),
        ),
        migrations.AddField(
            model_name='peminjaman',
            name='peminjam_username',
            field=models.ForeignKey(to='peminjaman.Peminjam'),
        ),
        migrations.AddField(
            model_name='approval',
            name='pengawas_username',
            field=models.ForeignKey(to='peminjaman.Pengawas'),
        ),
    ]
