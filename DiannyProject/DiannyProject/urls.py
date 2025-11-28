# ========================================================
# PUNTO I: CONFIGURACIÓN DE URLs PRINCIPALES
# Rutas para admin y página principal del proyecto
# ========================================================


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("miapp.urls")),
]
