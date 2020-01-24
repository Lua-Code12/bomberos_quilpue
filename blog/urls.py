from django.urls import path
from . import views, galeria


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
<<<<<<< HEAD
    path('galeria/', galeria, name="galeria")
=======
    path('galeria/', views.galeria, name="galeria")
>>>>>>> 42839a7199b522f17a869464b169e67257e9dfac
]
