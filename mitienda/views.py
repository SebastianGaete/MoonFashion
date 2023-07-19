from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poleron, Interesado
# Create your views here.


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'pages/about.html')


def catalogo(request):
    polerones: object = Poleron.objects.all()
    CONTEXT: dict = {
        'polerones':polerones
    }
    return render(request, 'pages/catalogo.html', CONTEXT)


def detail_catalogo(request, id):
    detalle: object = Poleron.objects.get(id=id)
    CONTEXT: dict ={
        'detalle':detalle
    } 
    return render(request, 'pages/detail_catalogo.html', CONTEXT)



def contact(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        tipo_entrega = request.POST['tipo_entrega']
        mensaje = request.POST['mensaje']

        interesado = Interesado.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, email=email, tipo_entrega= tipo_entrega, mensaje=mensaje)
        interesado.save()

        return redirect('envio_formulario') # SOLO SE INDICA LA PAGE A LA CUAL VAMOS A REDIRECCIONAR
    else:
         return render(request, 'pages/contact.html')
    

def envio_formulario(request):
    return render(request, 'pages/envio_formulario.html')


