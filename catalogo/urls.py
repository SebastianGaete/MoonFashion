from django.urls import path
from .views import *


urlpatterns = [
    path('productos/catalogo/<str:producto>/', catalogo_polerones, name='catalogo_productos'),
    path('detalle/producto/<int:id>/', detail_catalogo, name='detail_producto'),
]