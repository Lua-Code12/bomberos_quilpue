from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('galeria/', views.galeria, name="galeria"),
    path('formulario/', views.formulario, name="formulario"),
    path('vehiculos/', views.vehiculos, name="vehiculos"),
    path('listar_automoviles/', views.listar_automoviles, name='listar_autmoviles'),
    path('eliminar-auto/<id>/', views.eliminar_automovil, name="eliminar_automovil"),
   
]
