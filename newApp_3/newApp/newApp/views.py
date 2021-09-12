from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, User
from django.contrib.auth import logout, authenticate, login

def index(request):
    if(request.method == 'POST'):
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('ell_list:list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'is_auth': request.user.is_authenticated})

def about(request):
    return HttpResponse('about')

def signout(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'is_auth': request.user.is_authenticated})