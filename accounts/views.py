from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm

def singup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'singup.html', {'form':form , 'is_auth': request.user.is_authenticated})