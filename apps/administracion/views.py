from urllib import request
from django.shortcuts import render, redirect
from multiprocessing import context
from django.views import View
from apps.administracion.forms import Administracion
from apps.administracion.models import Cursos

# Create your views here.

class Administrar(View):
    def get(self,request):
        form = Administracion()
        cursos = Cursos.objects.all()       
        for i in cursos:
            print(i.curso_estado())
        context = {
            'form': form,
            'cursos':cursos
        }

        return render(request, 'administracion/addCurso.html', context)



    def post(self,request):
        if request.method == 'POST':
            form = Administracion(request.POST,request.FILES)
            if form.is_valid():
                form.save()
        return redirect('apps.administracion:addCurso')
            