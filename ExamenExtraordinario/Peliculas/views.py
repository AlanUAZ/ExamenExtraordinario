from django.shortcuts import render, redirect, get_object_or_404
from Peliculas.models import Peliculas
from Peliculas.forms import PeliculasForm

# Create your views here.
def listar(request):
	peliculas = Peliculas.objects.all()
	return render(request, 'Peliculas/lista.html', {'Peliculas':peliculas})

def agregar(request):
	if request.method == "POST":
		form = PeliculasForm(request.POST)
		print request.POST
		if form.is_valid():
			pelicula = form.save()
			pelicula.save()
			return redirect('Peliculas.views.listar')
	else:
		form = PeliculasForm
	return render(request,'Peliculas/pelicula_nueva.html',{'form':form, 'etiqueta':'Nueva'})

def eliminar(request, pk):
	peliculas = get_object_or_404(Peliculas, pk=pk)
	peliculas.delete()
	return redirect('listar')

def editar(request, pk):
	peliculas = get_object_or_404(Peliculas, pk = pk)
	if request.method == "POST":
		form = PeliculasForm(request.POST, instance = peliculas)
		print request.POST
		if form.is_valid():
			peliculas = form.save()
			peliculas.save()
			return redirect('lista')
	else:
		form = PeliculasForm (instance=peliculas)
	return render(request,'Peliculas/pelicula_nueva.html',{'form':form, 'etiqueta':'Actualizar'})