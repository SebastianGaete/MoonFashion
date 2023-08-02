from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about_comentario, name='about'),
    path('envio/satisfactorio/', envio_formulario, name='envio_formulario'),
]