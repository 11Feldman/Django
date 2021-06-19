from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect



# Create your views here.
class NewTasks(forms.Form):
    tarea = forms.CharField(label='')

def index(request):
    # Chequear si ya existe una clave “tareas” en nuestra sesion
    if "tareas" not in request.session:
        request.session["tareas"] = []
    return render(request, 'tasks/index.html', {
        'tasks': request.session["tareas"],
        'typeTask': 'tareas'
    })

def add(request):
    if request.method == 'POST':
        form = NewTasks(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data['tarea']
            request.session["tareas"]+= [tarea]
            return HttpResponseRedirect(reverse('TAREAS:index'))
        else:
            return render(request, 'tasks/add.html',{
                "formulario_de_alta": form
            })
    else:
        return render(request, 'tasks/add.html', {
            "formulario_de_alta": NewTasks()
        })
