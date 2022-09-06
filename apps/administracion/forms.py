from django import forms


class Administracion(forms.Form):
    def char(place):
        return  forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'2', 
            'placeholder':place,
            'class':'form-control'
            }), required=True, max_length=250, label='')

    nombre = char('Nombre del curso'),
    desc = char('Descripcion'),
    disertante = char('Nombre del disertante')
    precio = char('Precio')
    fecha_curso = forms.DateField()
    fecha_finalizacion = forms.DateField()
    dis_imagen = forms.ImageField()
    imagen = forms.ImageField()

