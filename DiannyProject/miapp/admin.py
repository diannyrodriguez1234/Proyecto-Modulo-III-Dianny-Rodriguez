# ========================================================
# PUNTO H: CONFIGURACIÓN DJANGO ADMIN
# Registro del modelo para gestión en /admin/
# ========================================================


from django.contrib import admin
from .models import Actividad

admin.site.register(Actividad)
