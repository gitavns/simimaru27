import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from peminjaman.models import Peminjaman
#from reportlab.pdfgen import canvas

# Create your views here.

def index(request):
    return render(request, 'peminjaman.html', '')


def history(request):
    if request.method == 'POST':
        mulai = request.POST.get("start_date")
        selesai = request.POST.get("end_date")
        data = {
            'peminjaman': Peminjaman.objects.filter(tanggal__range=(mulai,selesai)),
            'mulai' : mulai,
            'selesai' : selesai
        }
    else:
        data = {
            'peminjaman': Peminjaman.objects.filter(tanggal__month=datetime.datetime.now().month,
                                                    tanggal__year=datetime.datetime.now().year)
        }
    return render(request, 'history.html', data)

def export(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas("D:\form.pdf", pagesize='letter')

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    return p


def ruangan(request):
    return render(request, 'createnew.html', '')


def create(request):
    return render(request, 'formpeminjaman.html', '')
