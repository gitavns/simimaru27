__author__ = 'Addin'

import datetime
from django.http import HttpRequest
from django.shortcuts import render
from django.forms import ModelForm
from peminjaman.models import Peminjaman

# Create your views here.

def login(request):
    return render(request, 'teslogin.html', '')
def auth(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/peminjaman')
    return render_to_response('login.html', context_instance=RequestContext(request))
