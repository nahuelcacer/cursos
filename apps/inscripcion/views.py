from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.views import View
from apps.administracion.models import Cursos
from apps.inscripcion.models import Inscripciones
from apps.inscripcion.forms import Inscripcion


# SDK de Mercado Pago
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK("TEST-3189877754485702-090914-7182f92c2075e9fce5b9ba0f34445232-1195365420")

    
class Inscribirse(View):
    def get(self,request,id):
        curso = Cursos.objects.get(id=id)  
        fecha = curso.fecha_curso.strftime('%d/%m/%Y')
        form = Inscripcion()

        preference_data = {
            "items": [
                {
                    "title": curso.nombre,
                    "quantity": 1,
                    "unit_price": int(curso.precio),
                }
                ],
            "auto_return": "approved",
            "back_urls": {
                "success": 'http://127.0.0.1:8000/inscripcion/' + str(id),
                "failure": "http://www.failure.com",
                "pending": "http://www.pending.com"
                },
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        res = list(request.GET.items())
        if(len(res)>0):
            print(dict(request.GET.items()))
        
        context = {
            'curso':curso,
            'fecha':fecha,
            'form':form,
            'pay':preference
            
        }
        return render(request, 'inscripcion/inscribirse.html', context)
    
    # def post(self,request,id):
    #     form = Inscripcion(request.POST,request.FILES)
    #     curso =  Cursos.objects.get(id=id)
    #     if request.method == "POST":
    #         if form.is_valid():
    #             aux = form.save(commit=False)
    #             aux.curso = curso
    #             # aux.save()

    #             return redirect('apps.inscripcion:pay', id)

class Listar(View):
    def get(self,request,id):
        if request.user.is_authenticated:

            inscriptos = Inscripciones.objects.filter(curso=id)
            curso = Cursos.objects.get(id=id)
            fecha = curso.fecha_curso.strftime('%d/%m/%Y')
            context = {
                'inscriptos':inscriptos,
                'curso':curso,
                'fecha':fecha
            }
            return render(request,'inscripcion/listar.html', context)
        else:
            return redirect('/')

class Pay(View):
    def get(self,request,id):
        curso = Cursos.objects.get(id=id)
       
        # print(preference)
        return render(request,'inscripcion/pay.html')