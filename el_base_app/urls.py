from django.contrib import admin
from django.urls import path
from el_base_app import views
from el_base_app.views import ResistorListView
from django.conf.urls import url, include
from . import views


urlpatterns = [
  #  path('', ResistorListView.as_view(), name='resistors'),
    url(r'^$', views.index, name='index'),
    url(r'^$', admin.site.urls),
    url(r'^$', include('el_base_app.urls')),

]
