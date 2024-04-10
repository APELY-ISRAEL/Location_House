from django.shortcuts import redirect, render
from auth_app.models import User 
from auth_app.views import logout1
from .models import Client
from django.contrib.auth.decorators import login_required


def home(request):
        return render(request, 'home.html')

def login(request):
    if request.user.is_authenticated:
        # Utilisateur connecté, transmettre l'objet User au template
        return render(request, 'home.html', {'user': request.user})
    else:
        # Utilisateur non connecté, transmettre un objet vide ou autre selon vos besoins
        return render(request, 'login.html', {'user': None})
   
def house(request):
    return render(request, 'house.html')

def contact(request):
    return render(request, 'contact.html')

def category(request):
    return render(request, 'category.html')

@login_required
def profil(request):
    # Vous pouvez accéder aux informations de l'utilisateur connecté via request.user
    username = request.user.username
    email = request.user.email
    role = request.user.role  # Supposons que vous avez un champ 'role' dans votre modèle utilisateur

    # Maintenant vous pouvez passer ces informations au template
    return render(request, 'profil.html', {'username': username, 'email': email, 'role': role})

def logout(request):
    logout1(request)
    return redirect('home')