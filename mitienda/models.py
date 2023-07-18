from django.db import models

# Create your models here.

class Poleron(models.Model):
    TALLAS = [
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('EG','EG')
    ]
    marca = models.CharField(max_length=200, verbose_name='Marca')
    descripcion = models.TextField(blank=False, verbose_name='Descripción')
    talla = models.CharField(max_length=2, choices=TALLAS, verbose_name='Tallas')
    precio = models.CharField(max_length=20, verbose_name='Precio')
    stock = models.IntegerField(default=1, verbose_name='Stock')
    imagen = models.ImageField(blank=False, upload_to='polerones/images', verbose_name='Imagen')

    def __str__(self):
        return 'Poleron ' + self.marca
    
    class Meta():
        verbose_name = 'Polerones'


class Interesado(models.Model):
    
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    apellido = models.CharField(max_length=200, verbose_name='Apellido')
    telefono = models.IntegerField(verbose_name='Número de teléfono')
    email = models.EmailField(verbose_name='Email')
    tipo_entrega = models.CharField(max_length=100, verbose_name='Tipo de entrega')
    mensaje = models.TextField(verbose_name='Mensaje', default='Sin mensaje')
    fecha_solicitud = models.DateField(auto_now_add=True, verbose_name='Fecha de solicitud')
