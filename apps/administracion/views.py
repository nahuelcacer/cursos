from django.shortcuts import render, redirect
from multiprocessing import context
from django.views import View
from apps.administracion.forms import Administracion

# Create your views here.

class Administrar(View):
    def get(self,request):
        form = Administracion()
        context = {
            'form': form
            }

        return render(request, 'administracion/addCurso.html', context)