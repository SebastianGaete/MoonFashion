from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(primary_key=True, max_length=40, verbose_name='Nombre')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    def __str__(self):
        return self.nombre
       

class Productos(models.Model):
    TALLAS = [
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('EG','EG')
    ]
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, to_field='nombre', verbose_name='Categoria')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    descripcion = models.TextField(blank=False, verbose_name='Descripción')
    talla = models.CharField(max_length=2, choices=TALLAS, verbose_name='Tallas')
    precio = models.CharField(max_length=20, verbose_name='Precio')
    stock = models.IntegerField(default=1, verbose_name='Stock')
    imagen = models.ImageField(blank=False, upload_to='prendas_catalogo', verbose_name='Imagen')

    def __str__(self):
        return self.marca
    

