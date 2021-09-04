from django.contrib import admin
from django.urls import path
from el_base_app import views
from el_base_app.views import ResistorListView

urlpatterns = [
    path('', ResistorListView.as_view(), name='resistors'),

]
