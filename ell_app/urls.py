from django.contrib import admin
from django.urls import path, re_path
from ell_app import views

app_name = 'ell_list'

urlpatterns = [
    path('', views.ell_list, name='list'),
    re_path(r'(?P<type>\w{0,50})/$', views.get_list, name='get_table'),
]