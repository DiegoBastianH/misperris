from django.shortcuts import render
from django.utils import timezone
from . models import formulariopersona
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from FormularioPersona.forms import RegistroForm
from django.views.generic import CreateView

def pagina_principal(request):
	return render(request,'PaginaDelMisPerris/PaginaPrincipal.html')


def pagina_contactanos(request):
	form = formulariopersona()
	if request.method == "POST":
		form.CorreoElectronico = request.POST['correopers']
		form.Rut = request.POST['ruttt']
		form.NombreCompleto = request.POST['nombrepersona']
		form.FechaNacimiento = request.POST['Fechapers']
		form.Telefono = request.POST['telef']
		form.Direccion = request.POST['direcc']
		form.save()
	return render(request,'PaginaDelMisPerris/contactanos.html')


class RegistroUsuario(CreateView):
    model = User
    template_name = "PaginaDelMisPerris/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')

