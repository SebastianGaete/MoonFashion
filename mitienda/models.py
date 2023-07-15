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
    marca = models.CharField(max_length=200)
    descripcion = models.TextField(blank=False)
    talla = models.CharField(max_length=2, choices=TALLAS)
    precio = models.CharField(max_length=20)
    stock = models.IntegerField(default=1)
    imagen = models.ImageField(blank=False, upload_to='polerones/images')

    def __str__(self):
        return 'Poleron ' + self.marca
    
    class Meta():
        verbose_name = 'Polerones'

