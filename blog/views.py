from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Automovil, Marca
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

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


def listar_automoviles(request):

    autos = Automovil.objects.all()

    return render(request, 'blog/listar_automoviles.html', {
        'autos': autos
    })



def eliminar_automovil(request, id):
    #buscar el autimovil que se desea eliminar

    auto = Automovil.objects.get(id=id)

    try:
        auto.delete()
        mensaje = "Eliminado correctante"
        messages.success(request, mensaje)

    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)
    return redirect('listado_automoviles')


