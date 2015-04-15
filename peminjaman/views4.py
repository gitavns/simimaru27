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
    return render(request, 'login.html', '')

def importjadwal(request):
    return render(request, 'importjadwal.html', '')

def detail(request):
    if 'submit' in request.POST :
        id=request.POST.get("submit")
        Komentar.objects.create(peminjaman_id_id= id, komen=request.POST.get("komentar"), timestamp= datetime.datetime.now(), user_komentar_id = 'cs-05')
        p = Peminjaman.objects.filter(id=id)
        print 'masuk if'
    else :
        id=request.POST.get("id_peminjaman")
        p = Peminjaman.objects.filter(id=id)
        print "masuk else"

    data = {
            'komentar': Komentar.objects.filter(peminjaman_id=p[0].id),
            'peminjaman' : p
        }
    return render(request, 'detailpeminjaman.html', data)

def alur(request):
    return render(request, 'alurpeminjaman.html', '')

def baru(request):
    if request.method == 'POST' :
        Komentar.objects.create(peminjaman_id_id= 1, komen=request.POST.get("komentar"), timestamp= datetime.datetime.now(), user_komentar_id = 'cs-05')
    data = {
            'komentar': Komentar.objects.filter(peminjaman_id=(request.POST.get("id")))
        }
    return render(request, 'detailpeminjaman.html',data)

def auth(request):
    print('masuk')
    username = password = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        param = urllib.urlencode ({"username":username,"password":password})
        myrequest = urllib2.Request('https://apps.cs.ui.ac.id/webservice/login_ldap.php?%s' % (param))
        response = urllib2.urlopen(myrequest, timeout=1000000).read()
        arr = json.loads(response)
        
        if 'state' in arr:
            state = arr['state']
            print('state: ' + str(state))
