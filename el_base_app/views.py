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



class ResistorListView(ListView):
    model = Resistors
    # template_name =
    # resistance = resistance


def home(request):
    return render(request, 'html_code/home.html')

