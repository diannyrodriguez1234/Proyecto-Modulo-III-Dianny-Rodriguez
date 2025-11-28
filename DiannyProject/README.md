# Aplicación Web de Actividades – Módulo III

Proyecto desarrollado para el Módulo III del subproyecto **Desarrollo de aplicaciones I**.  
Consiste en una aplicación web con Django que permite gestionar un listado de actividades, usando modelos, vistas, plantillas y el panel de administración.

---

## Objetivo del proyecto

Implementar una aplicación web básica que:

- Use un modelo de base de datos para representar las actividades de enfoque del proyecto.
- Permita administrar las actividades desde el panel **Django Admin**.
- Muestre en una página web un listado de las actividades con su estado (completada o pendiente).

---

## Herramientas utilizadas

- **Lenguaje:** Python 3.x
- **Framework web:** Django 5.x
- **Editor:** Visual Studio Code
- **Control de versiones:** Git y GitHub
- **Sistema operativo:** Windows 10

---

## Pasos realizados (A–J)

1. **Instalación de herramientas (A)**

   - Instalación de Python, Visual Studio Code, Git y extensión de Python para VS Code.

2. **Entorno virtual (B)**

   - Creación del entorno virtual en la carpeta del proyecto:
     ```
     python -m venv venv
     ```
   - Activación del entorno virtual en Windows:
     ```
     venv\Scripts\activate
     ```

3. **Repositorio y control de versiones (C)**

   - Inicialización del repositorio Git en la carpeta del proyecto:
     ```
     git init
     ```
   - Configuración de nombre y correo para los commits.
   - Creación del repositorio remoto en GitHub y vinculación con el proyecto local.
   - Envío de los cambios al repositorio remoto con `git add`, `git commit` y `git push`.

4. **Instalación de Django y librerías (D)**

   - Instalación de Django dentro del entorno virtual:
     ```
     pip install django
     ```

5. **Creación del proyecto Django (E)**

   - Creación del proyecto principal:
     ```
     django-admin startproject DiannyProject .
     ```

6. **Creación del módulo (app) de la aplicación web (F)**

   - Creación de la app principal del proyecto:
     ```
     python manage.py startapp miapp
     ```
   - Registro de `miapp` en `INSTALLED_APPS` dentro de `DiannyProject/settings.py`.

7. **Modelos de la aplicación (G)**

   - Definición del modelo `Actividad` en `miapp/models.py` con campos como:
     - `titulo`
     - `fecha`
     - `completada`
   - Creación y aplicación de migraciones:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

8. **Configuración de Django Admin (H)**

   - Registro del modelo `Actividad` en `miapp/admin.py` para poder gestionarlo desde `/admin/`.
   - Creación de un superusuario para acceder al panel:
     ```
     python manage.py createsuperuser
     ```

9. **Vistas y plantillas (templates) (I)**

   - Creación de la vista `lista_actividades` en `miapp/views.py` que obtiene las actividades desde la base de datos y las envía al template.
   - Configuración de las rutas en `DiannyProject/urls.py` (y/o `miapp/urls.py`) para que la página principal muestre la lista de actividades.
   - Creación del template `miapp/templates/miapp/lista.html` que renderiza:
     - Título de la actividad.
     - Fecha.
     - Estado: ✓ Completada o ⏳ Pendiente.

10. **Listado de actividades de enfoque (J)**
    - La página principal muestra un listado de todas las actividades almacenadas en la base de datos.
    - Si no hay actividades, se muestra un mensaje informando “No hay actividades” y un enlace para ir al panel de administración y agregarlas.

---

## Cómo ejecutar el proyecto

1. Activar el entorno virtual:
   venv\Scripts\activate

text

2. Iniciar el servidor de desarrollo:
   python manage.py runserver

text

3. Abrir en el navegador:

- `http://127.0.0.1:8000/` → listado de actividades.
- `http://127.0.0.1:8000/admin/` → panel de administración (requiere usuario y contraseña).

---

## Autor

Desarrollado por **Dianny Rodriguez** como parte del Módulo III de la asignatura _Desarrollo de aplicaciones I_.
