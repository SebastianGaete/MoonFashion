from django.urls import path
from .views import *


urlpatterns = [
    path('catalogo/<str:producto>', catalogo_productos, name='catalogo_productos'),
    path('catalogo/producto/detalle/<int:id>', detail_catalogo, name='detail_producto')
]