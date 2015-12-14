# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from Empleado.models import Empleado
#from Empleado.forms import EmpleadoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def listar(request):
	empleados = Empleado.objects.all()
	return render(request, 'Empleado/lista.html', {'Empleado': empleados})