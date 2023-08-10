from django.db import models
from catalogo.models import Categoria
from django.contrib.auth.models import User
# Create your models here.

class Interesado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    telefono = models.CharField(max_length=50, verbose_name='Número de teléfono')
    email = models.EmailField(verbose_name='Email')
    tipo_entrega = models.CharField(max_length=60, verbose_name='Tipo de entrega')
    mensaje = models.TextField(verbose_name='Mensaje', default='Sin mensaje')
    fecha_solicitud = models.DateField(auto_now_add=True, verbose_name='Fecha de solicitud')


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='Usuario')
    cuerpo = models.TextField(null=False, blank=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)


class Presentacion_prenda(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='prendas_presentacion')
