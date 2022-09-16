from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms.widgets import DateInput, Input
from apps.inscripcion.models import Inscripciones, Pago


class Inscripcion(forms.ModelForm):
    
    class Meta:
        model = Inscripciones
        fields = ['nombre', 'dni', 'email']
        

class Pago(forms.ModelForm):
    class Meta:
        model = Pago
        fields = []