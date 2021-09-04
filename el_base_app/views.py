from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import EmbeddedElementBase
from .models import Resistors
from .models import Capacitor
from .models import Diode
from .models import Transistor
from .models import Chip
