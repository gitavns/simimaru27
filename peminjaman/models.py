from django.db import models

class Ruangan(models.Model):
    gedung = models.CharField(max_length=1)
    lantai = models.CharField(max_length=1)
    nomor = models.CharField(max_length=5)
    kapasitas = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    pesan = models.ManyToManyField('self', through='Pesan', symmetrical=False)

class Peminjam(User):
    nama = models.CharField(max_length=30)

class Pengawas(User):
    nama = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    nip = models.CharField(max_length=10,default=0)

class Manager_Ruangan(Peminjam):
    nip = models.CharField(max_length=10,default=0)

class Mahasiswa(Peminjam):
    npm = models.CharField(max_length=10,default=0)

class Peminjaman(models.Model):
    ruangan_id = models.ForeignKey(Ruangan)
    peminjam_username = models.ForeignKey(Peminjam)
    tanggal = models.DateField()
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    email = models.CharField(max_length=50)
    no_telp = models.CharField(max_length=13)
    nama_kegiatan = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=350)
    jumlah_peserta = models.IntegerField(default=0)
    approval_manager_ruangan = models.BooleanField()
    approval_pengawas = models.ManyToManyField(Pengawas,through='Approval')

class Komentar(models.Model):
    izin_id = models.ForeignKey(Peminjaman)
    pesan = models.CharField(max_length=140)
    timestamp = models.DateTimeField()
    user_komentar = models.ForeignKey(User)

class Pesan(models.Model):
    pengirim_username = models.ForeignKey(User, related_name='penerima_username')
    penerima_username = models.ForeignKey(User, related_name='pengirim_username')
    pesan = models.CharField(max_length=140)
    timestamp = models.DateTimeField()

class Approval(models.Model):
    pengawas_username = models.ForeignKey(Pengawas)
    izin_id = models.ForeignKey(Peminjaman)
    approval = models.BooleanField()