from django.urls import path, re_path
from . import views

app_name = 'apps.inscripcion'


urlpatterns = [
    path('<int:id>', views.Inscribirse.as_view(), name="inscribirse"),
    path('listar/<int:id>', views.Listar.as_view(), name="listar"),
    #pagar
    path(r'<int:id>/pay', views.Pay.as_view(),name="pay"),
]
