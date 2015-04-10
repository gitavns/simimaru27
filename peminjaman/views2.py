import datetime
from django.http import HttpRequest
from django.shortcuts import render
from django.forms import ModelForm
from peminjaman.models import Peminjaman
# Create your views here.

def index(request):
    return render(request, 'peminjaman.html', '')


def history(request):
    if request.method == 'POST':
        data = {
            'peminjaman': Peminjaman.objects.filter(tanggal__range=(request.POST.get("start_date"),request.POST.get("end_date")))
        }
    else:
        data = {
            'peminjaman': Peminjaman.objects.filter(tanggal__month=datetime.datetime.now().month,
                                                    tanggal__year=datetime.datetime.now().year)
        }
    return render(request, 'history.html', data)


def ruangan(request):
    return render(request, 'createnew.html', '')


def create(request):
    return render(request, 'formpeminjaman.html', '')

def sukses(request) :
    if request.method == 'POST' :
        p = Peminjaman(id = 2, tanggal=request.POST.get("tanggal"), waktu_mulai=request.POST.get("jam_awal"), waktu_selesai=request.POST.get("jam_akhir"), email=request.POST.get("email"), no_telp = request.POST.get("notelp"), nama_kegiatan = request.POST.get("namkeg"), deskripsi = request.POST.get("desk"), jumlah_peserta = request.POST.get("jumlah"), approval_manager_ruangan = False, ruangan_id_id = request.POST.get("ruangan_id"), peminjam_username_id = request.POST.get("user"))
        p.save()
        return render(request, 'sukses.html','')