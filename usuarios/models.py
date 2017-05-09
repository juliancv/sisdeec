from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
# Create your models here.

class Persona(models.Model):

    nombres     = models.CharField(max_length = 30)
    apellidos   = models.CharField(max_length = 50)
    identificacion = models.BigIntegerField(primary_key = True)
    telefono    = models.BigIntegerField()
    estado      = models.BooleanField(default = True)
    correo      = models.EmailField()
    Area_oficina = models.CharField(max_length = 40)
    usuario     = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.nombres

    @models.permalink
    def get_absolute_url():
        return ("detalles_persona", [self.identificacion])
