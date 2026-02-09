from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='home'),
    path('inventario/', views.lista_productos, name='lista'),
]
