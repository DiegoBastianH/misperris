from django.conf.urls import include, url
from . import views
from FormularioPersona.views import RegistroUsuario

urlpatterns = [
	url(r'^$', views.pagina_principal,  name='pagina_principal'),
	url(r'^contactanos/', views.pagina_contactanos,  name='pagina_contactanos'),

	url(r'^registrar/', RegistroUsuario.as_view(), name='pagina_registrar'),
]

