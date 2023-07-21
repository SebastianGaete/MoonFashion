from django.contrib import admin
from .models import Poleron, Polera, Chaqueta
# Register your models here.


@admin.register(Poleron)
class AdminPoleron(admin.ModelAdmin):
    list_display = ('marca', 'descripcion')

@admin.register(Polera)
class AdminPolera(admin.ModelAdmin):
    list_display = ('marca', 'descripcion')

@admin.register(Chaqueta)
class AdminChaqueta(admin.ModelAdmin):
    list_display = ('marca', 'descripcion')

    