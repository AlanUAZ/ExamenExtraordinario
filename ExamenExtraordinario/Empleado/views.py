# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from Empleado.models import Empleado
from Cliente.models import Cliente
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


@login_required
def listar(request):
    empleados = Empleado.objects.all()
    return render(request, 'Empleado/lista.html', {'Empleado': empleados})


def login_view(request):
    if request.user.is_authenticated():
       return render(request, 'Empleado/login.html', {})

    mensaje = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        empleado = Empleado.objects.get(user=request.user)
        if empleado is not None:
            return render(request, 'Peliculas/lista_empleado.html', {'mensaje': mensaje})
        else:
            cliente = Cliente.objects.get(user=request.user)
            return render(request, 'Peliculas/lista_cliente.html', {'mensaje': mensaje})
    else:
        mensaje = 'Nombre de usuario o contraseña no válido'
    return render(request, 'Empleado/login.html', {'mensaje': mensaje})
    {{}}

def cerrar(request):
    logout(request)
    return redirect('login_view')
