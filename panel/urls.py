from django.urls import path
from .views import *

urlpatterns = [
    path('', registro, name='registro'),
    path('logout/', cierre_sesion, name='logout'),
    path('login/', inicio_sesion, name='login')
]