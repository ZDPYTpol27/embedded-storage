from django.contrib import admin
from .models import Resistors, Chip, Capacitor, Diode, Transistor

admin.site.register(Resistors)
admin.site.register(Chip)
admin.site.register(Capacitor)
admin.site.register(Diode)
admin.site.register(Transistor)
# Register your models here.
