from django.contrib import admin
from .models import Poleron
# Register your models here.

@admin.register(Poleron)
class AdminPoleron(admin.ModelAdmin):
    list_display = ('marca', 'talla', 'precio', 'stock')