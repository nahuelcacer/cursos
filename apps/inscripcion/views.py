from django.shortcuts import redirect, render
from django.views import View
from apps.administracion.models import Cursos
from django.urls import reverse
from django.http import HttpResponse
# SDK de Mercado Pago
# import mercadopago
# # Agrega credenciales
# sdk = mercadopago.SDK("TEST-3189877754485702-090914-7182f92c2075e9fce5b9ba0f34445232-1195365420")
# Crea un ítem en la preferencia
# preference_data = {
        #     "items": [
        #         {
        #             "title": cursos.nombre,
        #             "quantity": 1,
        #             "unit_price": 1
        #             #  "unit_price": int(cursos.precio)
        #         }
        #     ],
        #     "back_urls": 
        #                         {
        #                             "success": "http://127.0.0.1:8000/inscripcion/",
        #                             "failure": "http://www.failure.com"                              
        #                         },
        
        #     "auto_return": "approved",
        #     "binary_mode": True
        # }

        # preference_response = sdk.preference().create(preference_data)
        # preference = preference_response["response"]
        # print(preference)

class Inscribirse(View):
    def get(self,request,id):
        curso = Cursos.objects.get(id=id)  
        fecha = curso.fecha_curso.strftime('%d/%m/%Y')
        context = {
            'curso':curso,
            'fecha':fecha
        }

        return render(request, 'inscripcion/inscribirse.html', context)