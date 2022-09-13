from multiprocessing import context
from django.shortcuts import render

from apps.administracion.models import Cursos
from datetime import date




def Index(request):
    cursos = Cursos.objects.all()
    ahora = date.today()
       
    context = {
        'cursos':cursos,
        'ahora':ahora
    }
    return render(request,'index.html', context)