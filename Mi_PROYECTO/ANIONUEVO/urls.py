from django.urls import path, include
# Llamamos al archivo de vistas de nuestra app para generarle
# las url que se pueden direccionar.
from . import views

app_name = 'ANIONUEVO'
urlpatterns = [
    path('', views.index, name="index")
]
