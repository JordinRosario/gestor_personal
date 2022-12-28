from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
# Create your views here.
def home(request):
    return render(request, 'home.html')


def edad_verificacion(request, edad):
    day = datetime.now()
    if edad >= 50:
        return render(request,'verific.html',{'day':day})
    
    elif edad >=18:
        return HttpResponse('<h1> Usted es mayor de edad <h1>')
    
    else:
        return HttpResponse('<h1>Usted es menor de edad<h1>')