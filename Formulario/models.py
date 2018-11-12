from django.db import models

# Create your models here.

class formularios(models.Model):

   NombrePerro=models.CharField(max_length=40)
   Raza=models.CharField(max_length=50)
   Descripcion=models.CharField(max_length=100)
   EstadoPerro2 = (
    ('1','Rescatado',),
    ('2', 'Adoptado'),
    ('3', 'Disponible'),
)
   EstadoPerro=models.CharField(max_length=40,choices=EstadoPerro2)

   image = models.FileField(upload_to='media')


class validacion(models.Model):
    formulario = models.ForeignKey(formularios, null=False, blank=False, on_delete=models.CASCADE)

