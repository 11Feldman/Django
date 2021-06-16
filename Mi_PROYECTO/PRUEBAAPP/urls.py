from django.urls import path, include
# Llamamos al archivo de vistas de nuestra app para generarle
# las url que se pueden direccionar.
from . import views

app_name = 'PRUEBAAPP'
urlpatterns = [
    path('', views.index, name="index"),
    path('cat', views.cat, name="helloCat"),
    path('saludar/<str:nombre>', views.saludoConNombre, name='saludoNombre'),
    path('saludoConHtml', views.saludoConHtml, name='SaludoConHTML'),
    path('miBlog', views.miBlog, name='MiBlog'),
    path('saludando/<str:nombre>', views.saludoConHtmlyVariable,
         name='saludoConHtmlyVariable'),
    path('layoutnew/<str:nombre>', views.layoutNew, name='LayOutNew')
]