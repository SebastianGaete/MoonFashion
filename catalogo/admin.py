from django.contrib import admin
<<<<<<< HEAD
from .models import Categoria, Producto
=======
from .models import Productos, Categoria
>>>>>>> master
# Register your models here.


@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
<<<<<<< HEAD
    readonly_fields = ('fecha_creacion',)

@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ('marca', 'categoria', 'talla', 'precio')
    list_editable = ('precio',)

=======


@admin.register(Productos)
class AdminProductos(admin.ModelAdmin):
    list_display = ('categoria', 'marca', 'precio', 'talla')
    list_editable = ('precio',)
>>>>>>> master

    