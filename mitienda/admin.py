from django.contrib import admin
from .models import Poleron, Interesado
# Register your models here.

@admin.register(Poleron)
class AdminPoleron(admin.ModelAdmin):
    list_display = ('marca', 'talla', 'precio', 'stock')


@admin.register(Interesado)
class AdminFormulario(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_solicitud', 'tipo_entrega')
    