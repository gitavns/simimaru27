from django.db import models

# Create your models here.

class ruangan(models.Model):
    gedung = models.CharField(max_length=1)
    lantai = models.CharField(max_length=1)
    nomor = models.CharField(max_length=5)
    kapasitas = models.IntegerField()

class user(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=30)
    nama = models.CharField(max_length=30)

class peminjam(models.Model):
    username = models.ForeignKey(user,primary_key=True)

class pengawas(models.Model):
    username = models.ForeignKey(user,primary_key=True)
    password = models.CharField(max_length=30)
    nama = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    nip = models.CharField(max_length=10,default=0)

class manager_ruangan(models.Model):
    username = models.ForeignKey(peminjam,primary_key=True)
    password = models.CharField(max_length=30)
    nama = models.CharField(max_length=30)
    nip = models.CharField(max_length=10,default=0)

class mahasiswa(models.Model):
    username = models.ForeignKey(peminjam,primary_key=True)
    password = models.CharField(max_length=30)
    nama = models.CharField(max_length=30)
    npm = models.CharField(max_length=10,default=0)

class peminjaman(models.Model):
    ruangan_id = models.ForeignKey(ruangan)
    peminjam_username = models.ForeignKey(peminjam)
    tanggal = models.DateField()
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    email = models.CharField(max_length=50)
    no_telp = models.CharField(max_length=13)
    nama_kegiatan = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=350)
    jumlah_peserta = models.IntegerField(default=0)
    approval_manager_ruangan = models.BooleanField()

class komentar(models.Model):
    izin_id = models.ForeignKey(peminjaman)
    pesan = models.CharField(max_length=140)
    timestamp = models.DateTimeField()
    user_komentar = models.ForeignKey(user)

class pesan(models.Model):
    pengirim_username = models.ForeignKey(user, related_name='penerima_username')
    penerima_username = models.ForeignKey(user, related_name='pengirim_username')
    pesan = models.CharField(max_length=140)
    timestamp = models.DateTimeField()


class approval_pengawas(models.Model):
    pengawas_username = models.ForeignKey(pengawas)
    izin_id = models.ForeignKey(peminjaman)
    approval = models.BooleanField()