from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100, verbose_name='Nombre')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    TALLAS = [
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('EG','EG')
    ]
    categoria = models.ForeignKey(Categoria, to_field='nombre', on_delete=models.RESTRICT, verbose_name='Categoria')
    marca = models.CharField(max_length=200, verbose_name='Marca')
    descripcion = models.TextField(blank=False, verbose_name='Descripción')
    talla = models.CharField(max_length=2, choices=TALLAS, verbose_name='Tallas')
    precio = models.CharField(max_length=30, verbose_name='Precio')
    stock = models.IntegerField(default=1, verbose_name='Stock')
    imagen = models.ImageField(blank=False, upload_to='productos', verbose_name='Imagen')

    def __str__(self):
        return  self.marca
    
