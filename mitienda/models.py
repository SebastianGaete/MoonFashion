from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Interesado(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    apellido = models.CharField(max_length=200, verbose_name='Apellido')
    telefono = models.CharField(verbose_name='Número de teléfono')
    email = models.EmailField(verbose_name='Email')
    tipo_entrega = models.CharField(max_length=100, verbose_name='Tipo de entrega')
    mensaje = models.TextField(verbose_name='Mensaje', default='Sin mensaje')
    fecha_solicitud = models.DateField(auto_now_add=True, verbose_name='Fecha de solicitud')


class Comentario(models.Model):
    pass