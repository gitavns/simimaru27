from django.db import models

# Create your models here.

class ruangan(models.Model):
    gedung = models.CharField(max_length=1)
    lantai = models.CharField(max_length=1)
    nomor = models.CharField(max_length=5)
    kapasitas = models.IntegerField()

class peminjaman(models.Model):
    ruangan_id = models.ForeignKey(ruangan)
    tanggal = models.DateField()
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    email = models.CharField(max_length=50)
    no_telp = models.CharField(max_length=13)
    nama_kegiatan = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=350)
    jumlah_peserta = models.IntegerField()
    approval_manager_ruangan = models.BooleanField()

class komentar(models.Model):
    izin_id = models.ForeignKey(peminjaman)
    pesan = models.CharField(max_length=140)
    timestamp = models.DateTimeField()

