from django.shortcuts import redirect, render
from admin_app.models import Maison
from auth_app.models import User 
from django.contrib.auth.decorators import login_required


def home(request):
        return render(request, 'home.html')
   
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

def maisons(request):
    maisons = Maison.objects.all()
    context = {'maisons': maisons}
    return render(request, 'house.html', context)
