from django.db import models
from apps.administracion.models import Cursos

# Create your models here.

class Inscripciones(models.Model):
    curso = models.ForeignKey(Cursos, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=250)
    dni = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    #datos_pago

class Pago(models.Model):
    payment_id = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    payment_type = models.CharField(max_length=250)
    order_id = models.CharField(max_length=250)
