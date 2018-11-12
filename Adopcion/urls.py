from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^intro/', views.pagina_intro,  name='pagina_intro'),

]

