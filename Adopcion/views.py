from django.shortcuts import render
from django.utils import timezone
from . models import adopcionperro


def pagina_intro(request):
	form = adopcionperro()
	if request.method == "POST":
		form.NombrePerroAdop = request.POST['nombreperroadop']
		form.CorreoAdop = request.POST['correoadop']
		form.RutAdop = request.POST['rutadop']
		form.DireccionAdop = request.POST['direccionadop']
		form.TelefonoAdop = request.POST['teleadop']
		form.save()
	return render(request,'PaginaDelMisPerris/intro.html')

