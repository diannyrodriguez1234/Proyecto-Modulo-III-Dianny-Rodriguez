# ========================================================
# PUNTO I-J: VISTAS Y LISTADO DE ACTIVIDADES
# Obtiene actividades de BD y las renderiza en template
# ========================================================


from django.shortcuts import render
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all().order_by('-fecha_ingreso')
    return render(request, "miapp/lista.html", {"productos": productos})
