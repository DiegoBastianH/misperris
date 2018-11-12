from django.db import models

# Create your models here.

class adopcionperro(models.Model):

   NombrePerroAdop = models.CharField(max_length=40)
   CorreoAdop = models.CharField(max_length=50)
   RutAdop = models.CharField(max_length=60)
   DireccionAdop = models.CharField(max_length=9)
   TelefonoAdop = models.CharField(max_length=20)

