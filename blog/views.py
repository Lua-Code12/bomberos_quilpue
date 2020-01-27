from django.shortcuts import render
from django.utils import timezone
from .models import Post, Marca, Automovil
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def galeria(request):
    return render(request, 'blog/galeria.html')

def formulario(request):
    return render(request, 'blog/formulario.html')


def vehiculos(request):
    return render(request, 'blog/vehiculos.html')


#CRUD de automoviles

autos = Automovil.objects.all()

def listar_automoviles(request):
    return render(request, 'blog/listar_automoviles.html', autos)
    {
        'autos': autos
    }