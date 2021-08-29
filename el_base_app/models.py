
from django.db import models


class EmbeddedElementBase(models.Model):
     dimensions = models.FloatField()
     number_of_pcs = models.IntegerField()
     row = models.IntegerField()
     rack = models.IntegerField()
     shelf = models.IntegerField()
     box = models.IntegerField()
     body_type = models.CharField(max_length=5)

     class Meta:
        abstract = True


class Resistors(EmbeddedElementBase):
     UNIT_OM = 'om'
     UNIT_KOM = 'kom'
     UNIT_MOM = 'mom'

     UNIT_CHOICES = (
         (UNIT_OM, UNIT_OM),
         (UNIT_KOM, UNIT_KOM),
         (UNIT_MOM, UNIT_MOM),
     )

     resistance = models.FloatField()
     unit = models.CharField(max_length=5, choices=UNIT_CHOICES)
     deviation = models.FloatField()
     power_dissipation = models.FloatField()



# Resistors(unit=Resistors.UNIT_OM)
# Resistors(unit='om')


class Capacitor(EmbeddedElementBase):
     UNIT_PF = 'pF'
     UNIT_NF = 'nF'
     UNIT_MKF = 'mkF'

     UNIT_CHOICES = (
        (UNIT_PF, UNIT_PF),
        (UNIT_NF, UNIT_NF),
        (UNIT_MKF, UNIT_MKF),
     )

     capacity = models.FloatField()
     unit = models.CharField(max_length=5)  # pf lub nf lub mkf
     voltage = models.IntegerField()


class Diode(EmbeddedElementBase):
     name = models.CharField(max_length=20)
     maximum_voltage = models.IntegerField()
     maximum_current = models.IntegerField()


class Transistor(EmbeddedElementBase):
     name = models.CharField(max_length=20)
     junction_type = models.CharField(max_length=5)  # pnp lub npn
     maximum_voltage = models.IntegerField()
     collector_current = models.IntegerField()
     gain = models.IntegerField()


class Chip(EmbeddedElementBase):
     name = models.CharField(max_length=20)
     microcircuit_type = models.CharField(max_length=10)  # analog lub digital
