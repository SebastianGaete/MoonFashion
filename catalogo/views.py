<<<<<<< HEAD
from django.shortcuts import render, redirect

from .models import Producto
=======
from django.shortcuts import render
from .models import Categoria, Productos
>>>>>>> master

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def catalogo_productos(request, producto):
    if producto == 'polerones':
<<<<<<< HEAD
        poleron = Producto.objects.filter(categoria='polerones')
        return render(request, 'catalogo_productos.html', {'productos':poleron})
    elif producto =='poleras':
        polera = Producto.objects.filter(categoria='poleras')
        return render(request, 'catalogo_productos.html', {'productos':polera})
    elif producto == 'chaquetas':
        chaqueta = Producto.objects.filter(categoria='chaquetas')
        return render(request, 'catalogo_productos.html', {'productos':chaqueta})
=======
        poleron = Productos.objects.filter(categoria=1)
        return render(request, 'catalogo_productos.html', {'productos':poleron})
    
    elif producto =='poleras':
        polera = Productos.objects.filter(categoria=2)
        return render(request, 'catalogo_productos.html', {'productos':polera})
    
    elif producto == 'chaquetas':
        chaqueta = Productos.objects.filter(categoria=3)
        if chaqueta:
            return render(request, 'catalogo_productos.html', {'productos':chaqueta})
>>>>>>> master
    

@login_required
def detail_catalogo(request, id):
<<<<<<< HEAD
    detalle_producto = Producto.objects.get(id=id)
    return render(request, 'detail_producto.html', {'detalle':detalle_producto})

=======
    detalle_producto = Productos.objects.get(id=id)
    return render(request, 'detail_producto.html', {'detalle':detalle_producto})
>>>>>>> master
