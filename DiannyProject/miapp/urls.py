from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_actividades, name='home'),
    path('actividades/', views.lista_actividades, name='lista'),
]
