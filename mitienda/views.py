from django.shortcuts import render
from django.http import HttpResponse
from .models import Poleron
# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')


def catalogo(request):
    polerones: object = Poleron.objects.all()
    CONTEXT: dict = {
        'polerones':polerones
    }
    return render(request, 'pages/catalogo.html', CONTEXT)


def detail_catalogo(request, id):
    detalle: object = Poleron.objects.get(id=id)
    CONTEXT: dict ={
        'detalle':detalle
    } 
    return render(request, 'pages/detail_catalogo.html', CONTEXT)
