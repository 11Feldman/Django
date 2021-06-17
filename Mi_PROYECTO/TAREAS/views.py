from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Usando session para tomar los datos.
class NewTask(forms.Form):
    tarea = forms.CharField(label='')

def index(request):
    if 'tareas' not in request.session:
        request.session['tareas'] = []
    return render(request, 'tasks/index.html', {
        'tasks': request.session['tareas'],
        'typeTask': 'tareas'
    })

def add(request):
    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data['tarea']
            request.session['tareas'] += [tarea]
            return HttpResponseRedirect(reverse('TAREAS:index'))
        else:
            return render(request, 'tasks/add.html',{
                'formulario_de_alta': form
            })
    else:
        return render(request, 'tasks/add.html', {
            "formulario_de_alta": NewTask()
        })