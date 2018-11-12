from django.shortcuts import render
from django.utils import timezone
from . models import formularios

def pagina_principal(request):
	return render(request,'PaginaDelMisPerris/PaginaPrincipal.html')
def pagina_servicios(request):
	return render(request,'PaginaDelMisPerris/servicios.html')

def pagina_quienessomos(request):
	return render(request,'PaginaDelMisPerris/quienessomos.html')

def pagina_agregarperro(request):
	form = formularios()
	if request.method == "POST" and request.FILES:
		form.NombrePerro = request.POST['nompe']
		form.Raza = request.POST['raza']
		form.Descripcion = request.POST['descrip']
		form.EstadoPerro = request.POST['estpe']
		form.image = request.FILES['subirarchivo']
		form.save()
	return render(request,'PaginaDelMisPerris/agregarperro.html')



