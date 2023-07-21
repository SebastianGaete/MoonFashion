from django.shortcuts import render
from .models import Poleron, Chaqueta, Polera
# Create your views here.



def catalogo_polerones(request):
    polerones: object = Poleron.objects.all()
    return render(request, 'polerones/catalogo_polerones.html',{
        'polerones':polerones
    })


def detail_catalogo(request, id):
    detalle: object = Poleron.objects.get(id=id)
    return render(request, 'polerones/detail_poleron.html',{
        'detalle':detalle
    })



def catalogo_chaquetas(request):
    chaquetas = Chaqueta.objects.all()
    return render(request, 'chaquetas/catalogo_chaquetas.html',{
        'chaquetas':chaquetas
    })


def detail_chaqueta(request, id):
    detalle = Chaqueta.objects.get(id=id)
    return render(request, 'chaquetas/detail_chaqueta.html', {
        'detalle':detalle
    })




def catalogo_poleras(request):
    poleras = Polera.objects.all()
    return render(request, 'poleras/catalogo_poleras.html', {
        'poleras': poleras
    })


def detail_polera(request, id):
    detail = Polera.objects.get(id=id)
    return render(request, 'poleras/detail_polera.html', {
        'detalle':detail
    } )