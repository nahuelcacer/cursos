from django.shortcuts import render
from django.views import View
from apps.administracion.models import Cursos

          
# SDK de Mercado Pago
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK("TEST-3189877754485702-090914-7182f92c2075e9fce5b9ba0f34445232-1195365420")
# Crea un ítem en la preferencia

# Create your views here.
def pago(json):
    print(json)

class Inscribirse(View):
    def get(self,request):
        cursos = Cursos.objects.get(id=1)       
        preference_data = {
            "items": [
                {
                    "title": cursos.nombre,
                    "quantity": 1,
                    "unit_price": 1
                    #  "unit_price": int(cursos.precio)
                }
                
            ]
        #     "back_urls" : {
        #         "success": "apps.inscripcion:aprobado"
        #         # "failure": "http://localhost:8080/feedback",
        #         # "pending": "http://localhost:8080/feedback"
        #     },
        #     "auto_return": "approved"
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        print(preference)
        print(cursos.nombre, cursos.id)
        context = {
            'cursos':cursos,
            'preference': preference
        }

        return render(request, 'inscripcion/prueba.html', context)