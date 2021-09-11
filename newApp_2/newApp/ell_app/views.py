from django.shortcuts import render, redirect
from .models import Resistors, Diode, Chip, Capacitor, Transistor, EmbeddedElementBase
from django.db.models import Q
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
    searchline = request.GET.get('search', '')
    registros = []
    if searchline:
        registros = filter_list_by_type(type, searchline)
    else:
        registros = get_list_by_type(type)
    header = registros[0].header()
    return  render(request,'ell_app/ell_list.html', {'registros': registros, 'title': type, 'header':header, 'is_auth': request.user.is_authenticated})

def get_list_by_type(type):
    if (type == 'Diode'):
        return  Diode.objects.all()
    elif (type == 'Chip'):
        return Chip.objects.all()
    elif (type == 'Capacitor'):
        return Capacitor.objects.all()
    elif (type == 'Transistor'):
        return Transistor.objects.all()
    elif (type == 'Resistors'):
        return Resistors.objects.all()

def filter_list_by_type(type, searchline):
    if (type == 'Diode'):
        return  Diode.objects.filter(
            Q(name=searchline) |
            Q(maximum_voltage=searchline) |
            Q(maximum_current=searchline))
    elif (type == 'Chip'):
        return Chip.objects.filter(
            Q(name=searchline) |
            Q(microcircuit_type=searchline))
    elif (type == 'Capacitor'):
        return Capacitor.objects.filter(
            Q(capacity=searchline) |
            Q(voltage=searchline))
    elif (type == 'Transistor'):
        return Transistor.objects.filter(
            Q(name=searchline) |
            Q(junction_type=searchline)|
            Q(maximum_voltage=searchline)|
            Q(collector_current=searchline)|
            Q(gain=searchline))
    elif (type == 'Resistors'):
        return Resistors.objects.filter(
            Q(resistance=searchline) |
            Q(deviation=searchline)|
            Q(power_dissipation=searchline))