from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

def inicio(request):
    return render(request,'paginas/inicio.html')
def respuesta(request):
    return render(request,'paginas/pagina.html')
def usuarios(request):
    usuarios=Usuario.objects.all()
    return render(request,'usuarios/index.html',{'usuarios':usuarios})
def servicios(request):
    return render(request,'paginas/servicios.html')
def crear(request):
    formulario=UsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario=formulario.save()
        return redirect('usuarios')
    return render(request,'usuarios/crear.html', {'formulario': formulario})
def editar(request,id):
    usuario=Usuario.objects.get(id=id)
    formulario=UsuarioForm(request.POST or None,request.FILES or None,instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request,'usuarios/editar.html', {'formulario':formulario})

def eliminar(request, id):
    usuario=Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')
# Create your views here.
