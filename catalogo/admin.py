from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.


@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    readonly_fields = ('fecha_creacion',)

@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ('marca', 'categoria', 'talla', 'precio')
    list_editable = ('precio',)


    