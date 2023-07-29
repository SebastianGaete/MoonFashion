from django.shortcuts import render
from .models import Categoria, Producto

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def catalogo_polerones(request):
    return render(request, 'catalogo_productos.html')

@login_required
def detail_catalogo(request):
    return render(request, 'detail_producto.html')


