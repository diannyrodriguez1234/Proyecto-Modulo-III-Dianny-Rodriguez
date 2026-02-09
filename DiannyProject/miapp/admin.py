# ========================================================
# PUNTO H: CONFIGURACIÓN DJANGO ADMIN
# Registro del modelo para gestión en /admin/
# ========================================================


from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'fecha_ingreso')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
