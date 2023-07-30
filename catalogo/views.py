from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Producto

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def catalogo_polerones(request, producto):
    if producto == 'polerones':
        poleron = Producto.objects.filter(categoria='polerones')
        return render(request, 'catalogo_productos.html', {'productos':poleron})
    elif producto =='poleras':
        polera = Producto.objects.filter(categoria='poleras')
        return render(request, 'catalogo_productos.html', {'productos':polera})
    elif producto == 'chaquetas':
        chaqueta = Producto.objects.filter(categoria='chaquetas')
        return render(request, 'catalogo_productos.html', {'productos':chaqueta})
    
@login_required
def detail_catalogo(request):
    return render(request, 'detail_producto.html')


