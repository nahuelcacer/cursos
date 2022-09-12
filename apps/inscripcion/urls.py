from django.urls import path, re_path
from . import views

app_name = 'apps.inscripcion'


urlpatterns = [
    path('<int:id>',views.Inscribirse.as_view(), name="inscribirse"),

]
