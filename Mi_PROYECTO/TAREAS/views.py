from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

tareas = ['Despertarse', 'Desayunar', 'Lanzar Robot', 'Banarse','Cocinar']


# Create your views here.
class NewTasks(forms.Form):
    tarea = forms.CharField(label='')

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': tareas,
        'typeTask': 'tareas'
    })

def add(request):
    #Chequear si el metodo en la vista es POST
    if request.method == 'POST':
        #Tomar los datos que el usuario ha enviado y guardarlo como un formulario
        form = NewTasks(request.POST)
        #Chequear si el formulario es valido desde el lado del servidor
        if form.is_valid():
            tarea = form.cleaned_data['tarea']
            tareas.append(tarea)
            #Redireccionar al usuario al indice
            return HttpResponseRedirect(reverse('TAREAS:index'))
        else:
            #Si el formulario es invalido, volver a renderizar la pagina web con la informacion existente
            return render(request, 'tasks/add.html',{
                "formulario_de_alta": form
            })
    else:
        return render(request, 'tasks/add.html', {
            "formulario_de_alta": NewTasks()
        })