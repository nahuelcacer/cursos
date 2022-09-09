from django.urls import path, re_path
from . import views

app_name = 'apps.inscripcion'


urlpatterns = [
    path('',views.Inscribirse.as_view(), name="inscribirse"),
    path('aprobado/',views.pago, name="aprobado")

]
