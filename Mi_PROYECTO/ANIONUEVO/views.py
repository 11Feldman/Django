from django.shortcuts import render
from datetime import datetime as dt

ahora = dt.now()
# Create your views here.
def index(request):
    #Variable de anio nuevo
    ahora = dt.now()
    return render(request, 'newyear/index.html',{
        'ahora': ahora.month == 1 and ahora.day == 1,
        'ahora2':  ahora
    })