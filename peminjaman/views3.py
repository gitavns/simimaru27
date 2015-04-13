import datetime
from django.http import HttpRequest
from django.shortcuts import render
from django.forms import ModelForm
from peminjaman.models import Peminjaman, Ruangan

# Create your views here.

def index(request):
    return render(request, 'peminjaman.html', "")


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
    if request.method == 'POST':
        tanggal = request.POST.get("date")
        mulai = request.POST.get("start_time")
        selesai = request.POST.get("end_time")
        data = {
            'peminjaman' : Peminjaman.objects.filter(tanggal=tanggal,waktu_mulai__range=(mulai,selesai),waktu_selesai__range=(mulai,selesai)),
            'peminjaman_partial':Peminjaman.objects.filter(tanggal=tanggal,waktu_mulai__range=(mulai,selesai)) or Peminjaman.objects.filter(tanggal=tanggal,waktu_selesai__range=(mulai,selesai)),
            'ruangan' : Ruangan.objects.all(),
            'post' : True,
            'date' : tanggal,
            'mulai' : mulai,
            'selesai' : selesai

        }
    else :
        data = {
            'peminjaman' : Peminjaman.objects.all(),
            'ruangan' : Ruangan.objects.all()
        }
    return render(request, 'createnew.html', data)

def create(request):
    return render(request, 'formpeminjaman.html', '')

def peminjaman(request):
    data = {
        'peminjaman' : Peminjaman.objects.all(),
        'haha': request.POST.get("username")
    }
    return render(request, 'peminjaman.html', data)
