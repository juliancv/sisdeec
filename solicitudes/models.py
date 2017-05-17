from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
# Create your models here.

class Actividad(models.Model):

    act_id    = models.AutoField(primary_key = True)
    solicitante_id  = models.ForeignKey(User, null = False,related_name='solicitante_id')
    responsable_id  = models.ForeignKey(User, null = True,related_name='responsable_id')
    titulo          = models.CharField(max_length = 50)
    prioridad       = models.IntegerField(null = True)
    resumen         = models.CharField(max_length = 500)
    estado          = models.CharField(max_length = 10)
    comentarios     = models.CharField(max_length = 500)
    fecha_solici    = models.DateField(default=timezone.now())
    fecha_final     = models.DateField(default=timezone.now())

    def __str__(self):
        return self.nombres

    @models.permalink
    def get_absolute_url():
        return ("detalles_actividad", [self.acticidad_id])
