from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .models import EmbeddedElementBase
from .models import Resistors
from .models import Capacitor
from .models import Diode
from .models import Transistor
from .models import Chip


# получение данных из бд
def index(request):
    people = Resistors.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Resistors()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")


class ResistorListView(ListView):
    model = Resistors
    template_name =