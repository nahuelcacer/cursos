from django.shortcuts import render, redirect
from multiprocessing import context
from django.views import View
from apps.administracion.forms import Administracion
from apps.administracion.models import Cursos

# Create your views here.

class Administrar(View):
    def get(self,request):
        cursos = Cursos.objects.all()
        print(cursos)
        form = Administracion()
        context = {
            'form': form,
            'cursos':cursos
        }

        return render(request, 'administracion/addCurso.html', context)

    def post(self,request):
        form = Administracion(request.POST)
        if form.is_valid():
            form.save()
        return redirect('apps.administracion:addCurso')  