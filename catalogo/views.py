from django.shortcuts import render
from .models import Poleron, Chaqueta, Polera

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def catalogo_polerones(request):
    polerones: object = Poleron.objects.all()
    return render(request, 'polerones/catalogo_polerones.html',{
        'polerones':polerones
    })

@login_required
def detail_catalogo(request, id):
    detalle: object = Poleron.objects.get(id=id)
    return render(request, 'polerones/detail_poleron.html',{
        'detalle':detalle
    })


@login_required
def catalogo_chaquetas(request):
    chaquetas = Chaqueta.objects.all()
    return render(request, 'chaquetas/catalogo_chaquetas.html',{
        'chaquetas':chaquetas
    })

@login_required
def detail_chaqueta(request, id):
    detalle = Chaqueta.objects.get(id=id)
    return render(request, 'chaquetas/detail_chaqueta.html', {
        'detalle':detalle
    })



@login_required
def catalogo_poleras(request):
    poleras = Polera.objects.all()
    return render(request, 'poleras/catalogo_poleras.html', {
        'poleras': poleras
    })


@login_required
def detail_polera(request, id):
    detail = Polera.objects.get(id=id)
    return render(request, 'poleras/detail_polera.html', {
        'detalle':detail
    } )