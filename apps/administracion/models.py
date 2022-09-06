from dataclasses import asdict
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.db import models

# Create your models here.


class Cursos(models.Model):
    nombre = models.CharField(max_length=250) # nombre
    desc = models.CharField(max_length=250) # descripcion
    disertante = models.CharField(max_length=100) # disertante
    fecha_curso = models.DateField() # fecha del curso
    fecha_finalizacion = models.DateField() # fecha de finalizacion de inscripcion
    precio = models.CharField(max_length=60)# precio
    dis_imagen = models.ImageField()# foto del disertante 
    imagen = models.ImageField() # imagen adicional 
    

    def curso_estado(self):
        import datetime
        if self.fecha_finalizacion > datetime.now():
            return ("Activo")
        else:
            return ("Inactivo")