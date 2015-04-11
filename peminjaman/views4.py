__author__ = 'Addin'

import datetime
import urllib
import urllib2
import json
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import render
from django.forms import ModelForm
from peminjaman.models import Peminjaman, Komentar

# Create your views here.

def login(request):
    return render(request, 'teslogin.html', '')

def detail(request):
    if request.method == 'POST':
        data = {
            'komentar': Komentar.objects.filter(peminjaman_id=(request.POST.get("id")))
        }
    else:
        data = {
            'komentar': Komentar.objects.all()
        }
    return render(request, 'detailpeminjaman.html', data)

def suksesdetail(request) :
    if request.method == 'POST':
        k = Komentar(id = 3, peminjaman_id= 1, komen=request.POST.get("komentar"), timestamp=request.POST.get(datetime), user_komentar_id=1)
        k.save()
    return render(request, 'history.html','')
def auth(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        param = urllib.urlencode ({"username":username,"password":password})
        myrequest = urllib2.Request('https://apps.cs.ui.ac.id/webservice/login_ldap.php?%s' % (param))
        response = urllib2.urlopen(myrequest, timeout=1000000).read()
        return render(request, 'index.html', response)
