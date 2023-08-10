from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Interesado, Comentario, Presentacion_prenda

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    prendas = Presentacion_prenda.objects.all()
    return render(request, 'index.html', {'prendas':prendas})


@login_required
def about_comentario(request):
    if request.method == 'POST':
        usuario = request.user
        cuerpo = request.POST['cuerpo']

        nuevo_comentario = Comentario.objects.create(usuario=usuario, cuerpo=cuerpo)
        nuevo_comentario.save()
        return redirect('about')

    comentarios = Comentario.objects.all().order_by('-fecha_publicacion')
    return render(request, 'pages/about.html', {'comentarios': comentarios})


@login_required
def contact(request):
    if request.method == 'POST':

        if len(request.POST['telefono']) == 10:
            try:
                nombre = request.POST['nombre']
                apellido = request.POST['apellido']
                telefono = request.POST['telefono']
                email = request.POST['email']
                tipo_entrega = request.POST['tipo_entrega']
                mensaje = request.POST['mensaje']

                interesado = Interesado.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, email=email, tipo_entrega= tipo_entrega, mensaje=mensaje)
                interesado.save()
                return redirect('envio_formulario') # SOLO SE INDICA LA PAGE A LA CUAL VAMOS A REDIRECCIONAR
        
            except:
                return render(request, 'pages/contact.html', {
                    'error': 'Porfavor procure ingresar los datos en el formato que se solicitan.'
                })
        else:
            return render(request, 'pages/contact.html', {
                    'error': 'Porfavor procure ingresar los datos en el formato que se solicitan.'
                })
    else:
         return render(request, 'pages/contact.html')
  
    
@login_required
def envio_formulario(request):
    return render(request, 'pages/envio_formulario.html')

