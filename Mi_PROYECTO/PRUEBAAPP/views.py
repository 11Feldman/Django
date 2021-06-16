#Importamos la funcionalidad que dibuja una pagina web
from django.shortcuts import render
#Importamos la funcionalidad que nos permite realizar comunicaciones usando el protocolo HTTP
from django.http import HttpResponse

# Creamos las vistas de nuestra app

# Vista index
def index(request):
    return HttpResponse("hola, mundo")

# Vista Cat
def cat(request):
    return HttpResponse("hola, cat")

# Vista prueba, pero con variable.
def saludoConNombre(request, nombre):
    #agrego f para que sea una cadena de caracteres.
    return HttpResponse(f'hola, {nombre.capitalize()}')

def saludoConHtml(request):
    return render(request, 'saludar/index.html')

def saludoConHtmlyVariable(request, nombre):
    return render(request, 'saludar/saludar.html',{
        'nombre': nombre.capitalize()
    })

def miBlog(request):
    return render(request, 'Miblog/index.html')

def layoutNew(request, nombre):
    return render(request, 'saludar/body.html')