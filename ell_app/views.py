from django.shortcuts import render, redirect
from .models import Resistors, Diode, Chip, Capacitor, Transistor, EmbeddedElementBase
from django.http import HttpResponse

# Create your views here.

def ell_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    registros = Resistors.objects.all()
    title = 'Resistors'
    header = registros[0].header()

    return  render(request,'ell_app/ell_list.html', {'registros': registros, 'title': title, 'header':header, 'is_auth':request.user.is_authenticated})

def get_list(request, type):
    if not request.user.is_authenticated:
        return redirect('login')
    title = type
    registros = []
    if(type == 'Diode'):
        registros = Diode.objects.all()
    elif (type == 'Chip'):
        registros = Chip.objects.all()
    elif (type == 'Capacitor'):
        registros = Capacitor.objects.all()
    elif (type == 'Transistor'):
        registros = Transistor.objects.all()
    elif (type == 'Resistors'):
        registros = Resistors.objects.all()
    header = registros[0].header()
    return  render(request,'ell_app/ell_list.html', {'registros': registros, 'title': title, 'header':header, 'is_auth': request.user.is_authenticated})