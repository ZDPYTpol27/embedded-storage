from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('lsit')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'is_auth': request.user.is_authenticated})

def about(request):
    return HttpResponse('about')