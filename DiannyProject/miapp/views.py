# ========================================================
# PUNTO I-J: VISTAS Y LISTADO DE ACTIVIDADES
# Obtiene actividades de BD y las renderiza en template
# ========================================================


from django.shortcuts import render
from .models import Actividad


def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, "miapp/lista.html", {"actividades": actividades})
