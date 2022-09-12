from multiprocessing import context
from django.shortcuts import render

from apps.administracion.models import Cursos




def Index(request):
    cursos = Cursos.objects.all()
    context = {
        'cursos':cursos
    }
    return render(request,'index.html', context)