<<<<<<< HEAD
from django.urls import path
from . import views, galeria

=======
from django.urls import path, include
from . import views
>>>>>>> 8125640c64cdb3f4d04ffe11240593e48523d492

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('galeria/', galeria, name="galeria")
=======
    path('galeria/', views.galeria, name="galeria")
>>>>>>> 42839a7199b522f17a869464b169e67257e9dfac
=======
    path('galeria', views.galeria, name="galeria")
   
>>>>>>> 8125640c64cdb3f4d04ffe11240593e48523d492
]
