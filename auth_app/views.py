from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from auth_app.models import User 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role')  # Ajoutez un champ pour sélectionner le rôle dans votre formulaire
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà utilisé.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email déjà utilisé.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, role=role)  # Ajoutez le rôle ici
        user.set_password(password)
        user.save()
        
        messages.success(request, 'Compte créé avec succès. Connectez-vous maintenant.')
        return redirect('login')
        
    return render(request, 'register.html')

def login1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil après connexion
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
    return render(request, 'login.html')

@login_required
def profil(request):
    return render(request, 'profil.html')

def logout1(request):
    logout(request)
    return redirect('login')  # Rediriger vers la page de connexion après déconnexion

def client_home(request):
    return render(request, 'home.html')

def admin_home(request):
    return render(request, 'index.html')

@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'client':
            return redirect('client_home')
        elif request.user.role == 'admin':
            return redirect('admin_home')
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')
