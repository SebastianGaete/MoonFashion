from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate


from django.db import IntegrityError
# Create your views here.

def registro(request):
    form = UserCreationForm()

    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form':form
        })
    
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            if password1 == password2:
                usuario = User.objects.create_user(username=username, password=password2)
                login(request, usuario)
                usuario.save()
                return redirect('home')
        
            else:
                return render(request, 'registro.html', {
                    'form':form,
                    'mensaje':'Las contraseñas no coinciden!'
                })
        except IntegrityError:
            return render(request, 'registro.html', {
                    'form':form,
                    'mensaje':'Usuario ya existente!'
                })


def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {
            'form':AuthenticationForm
        })
    
    else:
        username = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(request, username=username, password=password)

        try:
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                return render(request, 'inicio_sesion.html', {
                'form':AuthenticationForm,
                'mensaje':'Error de autentificación!'
            })

        except ValueError:
            return render(request, 'inicio_sesion.html', {
            'form':AuthenticationForm
        })


def cierre_sesion(request):
    logout(request)
    return redirect('login')
            

