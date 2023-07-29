from django.urls import path
from .views import *


urlpatterns = [
    path('catalogo/productos', catalogo_polerones, name='catalogo_productos'),
    path('detalle/producto', detail_catalogo, name='detail_producto'),
]