from django.shortcuts import render, redirect, get_object_or_404
from Renta.models import Renta
from Renta.forms import RentaForm
from Peliculas.models import Peliculas
from DetalleRenta.models import DetalleRenta
from datetime import datetime,timedelta
from Cliente.models import Cliente

# Create your views here.

def listar(request):
	rentas = Renta.objects.all()
	return render(request, 'Renta/lista.html', {'rentas':rentas})

def rentar(request):
    if request.method == "POST":
        cliente = Cliente.objects.get(user=request.user)
        if cliente is not None:
            renta = Renta(fecha=datetime.now(),cliente=cliente)
            Peliculas = request.POST.getlist('pelicula')
            print ("Ya esta creada la lista de peliculas")
            print (Peliculas)
            print (request.POST)			
            renta.save()
            for pelicula in Peliculas:
                print ("Empieza el for")
                pelicula_Temp = Peliculas.objects.get(id=pelicula)
                print (pelicula_Temp)				
                entrega= renta.fecha_renta + timedelta(days=3)
                detalle = DetalleRenta(fechaentrega=entrega,pelicula=pelicula_Temp,renta=renta)				
                detalle.save()
            return redirect('lista')
    else:
        form = RentaForm
    return render(request,'Renta/renta_nueva.html',{'form':form, 'etiqueta':'Nueva'})