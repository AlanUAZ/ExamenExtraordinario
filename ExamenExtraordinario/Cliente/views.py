# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from Cliente.models import Cliente

# Create your views here.

def listar(request):
	clientes = Cliente.objects.all()
	return render(request, 'Cliente/lista.html', {'Cliente': clientes})