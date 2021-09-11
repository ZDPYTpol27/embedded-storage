
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lists/', include('ell_app.urls'), name='list'),
    path('account/', include('accounts.urls')),
    path('about/', views.about),
    path('', views.index, name='login'),
]

urlpatterns += staticfiles_urlpatterns()