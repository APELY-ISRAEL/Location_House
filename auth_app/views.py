from django.shortcuts import render
from django.shortcuts import render, redirect
from auth_app.models import User 
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
       # Vérifier que le nom d'utilisateur n'est pas déjà utilisé
        if User.objects.filter(name=name).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà utiliser.')
            return redirect('login/')  # Remplacez 'registration/register.html' par votre propre modèle de formulaire d'inscription
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email déjà utilisé.')
            return redirect('login/')
        
          # Créer un nouvel utilisateur avec un mot de passe crypté
        user = User(name=name, email=email)
        user.set_password(password)  # Crypter le mot de passe
        user.save()
        
        messages.success(request, 'Compte creer avec succes.')
        return redirect('login/')  # Remplacez 'registration/register.html' par votre propre modèle de formulaire d'inscription
        
        
    return render(request, 'register.html')

def login1(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'email ou mot de passe incorrect.')
    return render(request, 'login.html')



def logout1(request):
    logout(request)
    return redirect('login')