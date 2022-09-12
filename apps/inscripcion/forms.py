from django import forms
from django.forms.widgets import DateInput, Input
from apps.inscripcion.models import Inscripciones


class Inscripcion(forms.ModelForm):
    
    class Meta:
        model = Inscripciones
        fields = ['nombre', 'dni', 'email']
        