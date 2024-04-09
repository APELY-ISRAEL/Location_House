from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from auth_app.models import User 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà utilisé.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email déjà utilisé.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        
        messages.success(request, 'Compte créé avec succès. Connectez-vous maintenant.')
        return redirect('login')
        
    return render(request, 'register.html')


def login1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil après connexion
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
    return render(request, 'login.html')


def logout1(request):
    logout(request)
    return redirect('login')  # Rediriger vers la page de connexion après déconnexion
