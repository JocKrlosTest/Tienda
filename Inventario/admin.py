from django.contrib import admin

from .models import Producto, Venta, Queja

# Register your models here.

@admin.register(Producto)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('nombre','precio','cantidad')
    ordering = ("precio",)

@admin.register(Venta)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('comprador','producto','cantidad')

@admin.register(Queja)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('usuario','asunto','fecha')