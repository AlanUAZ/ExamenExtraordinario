from django.shortcuts import render
from DetalleRenta.models import DetalleRenta

# Create your views here.
def listar(request):
	detalles = DetalleRenta.objects.all()
	return render(request, 'DetalleRenta/lista_detalle.html', {'detalles':detalles})