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
