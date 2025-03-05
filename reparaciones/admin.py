from django.contrib import admin
from .models import Cliente, OrdenReparacion

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'user', 'mostrar_contrasena')

    def mostrar_contrasena(self, obj):
        return "Se generó automáticamente (ver en shell)"
    mostrar_contrasena.short_description = "Contraseña"

@admin.register(OrdenReparacion)
class OrdenReparacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'cliente', 'item', 'fecha_ingreso')
    search_fields = ('codigo', 'cliente__username', 'item')
