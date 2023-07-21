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



class Chaqueta(models.Model):
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
    imagen = models.ImageField(blank=False, upload_to='chaquetas/images', verbose_name='Imagen')

    def __str__(self):
        return 'Chaqueta ' + self.marca
    
    class Meta():
        verbose_name = 'Chaquetas'




class Polera(models.Model):
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
    imagen = models.ImageField(blank=False, upload_to='poleras/images', verbose_name='Imagen')

    def __str__(self):
        return 'Polera ' + self.marca
    
    class Meta():
        verbose_name = 'Poleras'

