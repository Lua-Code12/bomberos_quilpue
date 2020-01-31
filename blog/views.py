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


def login(request):
    return render(request, 'sabores_patrios/login.html',{})



def vehiculos(request):

    marcas = Marca.objects.all()
    variables = {
        'marcas':marcas
    }

    if request.POST:
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = request.POST.get('txtAnio')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.marca = marca 

        try:
            auto.save()
            variables['mensajes'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se a podido guardar'
            

    return render(request, 'blog/vehiculos.html', variables)


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

    return redirect('listar_autmoviles')


def modificar_automovil(request, id):
    #buscamos el automovil para que el cuerpo de bomberos lo pueda modificar    
    auto = Automovil.objects.get(id=id)
    marcas = Marca.objects.all()
    variables = {
        'auto':auto,
        'marcas':marcas 

    }

    if request.POST:
        auto = Automovil()
        auto.id = request.POST.get('txtId')
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = request.POST.get('txtAnio')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.marca = marca 

        try:
            auto.save()
            messages.success(request, 'modificado correctamente')
        except:
            messages.error(request, 'no se ha podido modificar')
        return redirect('listar_autmoviles')
            

    return render(request, 'core/modificar_automovil.html', variables)