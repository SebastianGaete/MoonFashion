from django.shortcuts import render
from .models import Categoria, Productos

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def catalogo_productos(request, producto):
    if producto == 'polerones':
        poleron = Productos.objects.filter(categoria=1)
        return render(request, 'catalogo_productos.html', {'productos':poleron})
    
    elif producto =='poleras':
        polera = Productos.objects.filter(categoria=2)
        return render(request, 'catalogo_productos.html', {'productos':polera})
    
    elif producto == 'chaquetas':
        chaqueta = Productos.objects.filter(categoria=3)
        if chaqueta:
            return render(request, 'catalogo_productos.html', {'productos':chaqueta})
    

@login_required
def detail_catalogo(request, id):
    detalle_producto = Productos.objects.get(id=id)
    return render(request, 'detail_producto.html', {'detalle':detalle_producto})
