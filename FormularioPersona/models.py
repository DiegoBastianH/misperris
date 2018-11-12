from django.db import models

# Create your models here.

class formulariopersona(models.Model):

   CorreoElectronico=models.CharField(max_length=40)
   Rut = models.CharField(max_length=9)
   NombreCompleto=models.CharField(max_length=60)
   FechaNacimiento = models.DateField()
   Telefono = models.CharField(max_length=9)
   Direccion = models.CharField(max_length=20)

def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()
