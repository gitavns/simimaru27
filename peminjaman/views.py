from django.shortcuts import render
from django.forms import ModelForm

# Create your views here.

def index(request):
    return render(request, 'peminjaman.html', '')

def history(request):
    return render(request, 'history.html', '')

def ruangan(request):
    return render(request, 'createnew.html', '')

def create(request):
    return render(request, 'formpeminjaman.html', '')