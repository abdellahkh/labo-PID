from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Success"))
            return redirect('home')
        else:
            messages.success(request, ("I l y a une erreur, reessayer..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Vous etes deconnecte!"))
    return redirect('home')