# ========================================================
# PUNTO G: MODELOS DE LA APLICACIÓN WEB
# Modelo Actividad para gestionar tareas del proyecto
# ========================================================


from django.db import models


class Producto(models.Model):
    CATEGORIAS = [
        ('HW', 'Hardware'),
        ('SW', 'Software'),
        ('ACC', 'Accesorios'),
        ('RED', 'Redes'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.CharField(max_length=3, choices=CATEGORIAS, default='HW', verbose_name="Categoría")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Cantidad en Stock")
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"
