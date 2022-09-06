from django.urls import path, re_path
from . import views

app_name = 'apps.administracion'


urlpatterns = [
    path('addCurso/',views.Administrar.as_view( ), name="addCurso")
]
