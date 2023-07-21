from django.contrib import admin
from .models import Interesado
# Register your models here.


@admin.register(Interesado)
class AdminFormulario(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_solicitud', 'tipo_entrega')
    