from django.contrib import admin
from .models import Interesado, Comentario, Presentacion_prenda
# Register your models here.


@admin.register(Interesado)
class AdminFormulario(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_solicitud', 'tipo_entrega')
    

@admin.register(Comentario)
class AdminComentario(admin.ModelAdmin):
    readonly_fields = ('fecha_publicacion',)

@admin.register(Presentacion_prenda)
class AdminPresentacion_prenda(admin.ModelAdmin):
    pass

