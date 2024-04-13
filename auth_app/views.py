from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from auth_app.models import CustomUser

def register(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = 'client'  # Par défaut, nouvel utilisateur est un client

        # Créer un nouvel utilisateur
        user = CustomUser.objects.create_user(username=username, email=email, password=password, role=role)

        # Rediriger vers la page de connexion après l'inscription réussie
        return redirect('login')

    return render(request, 'register.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Vérifier si l'utilisateur existe dans la base de données
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:  # Vérifier si le compte est actif
                login(request, user)
                # Rediriger l'utilisateur vers la page appropriée
                if user.role == 'admin':
                    return redirect('index')
                elif user.role == 'client':
                    return redirect('home')
            else:
                # Compte inactif, afficher un message d'erreur
                messages.error(request, 'Votre compte est inactif.')
                return redirect('login')  # Redirection vers la page de connexion
        else:
            # Informer l'utilisateur que les informations de connexion sont incorrectes
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return redirect('login')  # Redirection vers la page de connexion

    return render(request, 'login.html')

def logout1(request):
    logout(request)
    return redirect('login')
