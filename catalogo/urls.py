from django.urls import path
from .views import *


urlpatterns = [
    path('polerones/catalogo/', catalogo_polerones, name='catalogo_polerones'),
    path('polerones/detail/<int:id>/', detail_catalogo, name='detail_poleron'),

    path('chaquetas/catalogo/', catalogo_chaquetas, name='catalogo_chaquetas'),
    path('chaquetas/detail/<int:id>/', detail_chaqueta, name='detail_chaqueta'),

    path('poleras/catalogo_poleras/', catalogo_poleras, name='catalogo_poleras'),
    path('poleras/detail/<int:id>/', detail_polera, name='detail_polera')
]