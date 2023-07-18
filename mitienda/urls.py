from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('catalogo/', catalogo, name='catalogo'),
    path('detail/<int:id>', detail_catalogo, name='detail_catalogo'),
    path('envio/satisfactorio', envio_formulario, name='envio_formulario')
]