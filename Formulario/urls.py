from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.pagina_principal,  name='pagina_principal'),
	url(r'^servicios/', views.pagina_servicios,  name='pagina_servicios'),
	url(r'^quienesssomos/', views.pagina_quienessomos,  name='pagina_quienessomos'),
	url(r'^agregarperro/', views.pagina_agregarperro,  name='pagina_agregarperro'),
]
