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