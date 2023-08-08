from django.contrib import admin
from .models import Productos, Categoria
# Register your models here.


@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')


@admin.register(Productos)
class AdminProductos(admin.ModelAdmin):
    list_display = ('categoria', 'marca', 'precio', 'talla')
    list_editable = ('precio',)

    