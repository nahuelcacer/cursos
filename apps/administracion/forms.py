from cProfile import label
from datetime import date
from tkinter.tix import InputOnly
from django import forms

from apps.administracion.models import Cursos
from django.forms.widgets import DateInput, Input

class Administracion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
                if field.label == "Fecha curso":
                    pass
                elif field.label == "Fecha finalizacion":
                    pass
                elif field.label == "Imagen":
                    field.label = "Banner o Imagen"
                    
                elif field.label == "Dis imagen":
                    field.label = "Imagen del disertante"
                else:
                    field.label = ""

    class Meta:
        model = Cursos
        fields = '__all__'
        widgets = {
            'fecha_curso': DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': DateInput(attrs={'type': 'date'}),
            'nombre': Input(attrs={ 
                                'placeholder':'Nombre del curso',
                                'class':'form-control'}),
            'desc': Input(attrs={ 
                                'placeholder':'Descripcion del curso',
                                'class':'form-control'}),
            'precio': Input(attrs={ 
                                'placeholder':'Precio del curso',
                                'class':'form-control'}),
            'disertante': Input(attrs={ 
                                'placeholder':'Disertante del curso',
                                'class':'form-control'}),
            
        }