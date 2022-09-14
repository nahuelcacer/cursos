from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Cursos(models.Model):
    nombre = models.CharField(max_length=250) # nombre
    desc = models.CharField(max_length=250) # descripcion
    disertante = models.CharField(max_length=100) # disertante
    fecha_curso = models.DateField() # fecha del curso
    fecha_finalizacion = models.DateField() # fecha de finalizacion de inscripcion
    precio = models.CharField(max_length=60)# precio
    dis_imagen = models.ImageField(upload_to="disertantes/",null=True)# foto del disertante 
    imagen = models.ImageField(upload_to="imagen/", null=True) # imagen adicional 
    

    def curso_estado(self):
        from datetime import date

        if self.fecha_finalizacion > date.today():
            return ("Activo")
        else:
            return ("Inactivo")