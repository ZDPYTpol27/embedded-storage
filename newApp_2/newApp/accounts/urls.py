from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('singup', views.singup, name='singup')
]