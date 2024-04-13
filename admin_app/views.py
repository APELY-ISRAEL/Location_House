from django.shortcuts import render

 

# Create your views here.


# Dans views.py de votre application (client_app, admin_app, etc.)

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'index.html')
       

# Autres vues comme client_dashboard, admin_dashboard, etc.
def ajout(request):
    return render(request, 'ajout.html')
def categorie(request):
    return render(request, 'categorie.html')
def liste(request):
    return render(request, 'liste.html')
def listeCat(request):
    return render(request, 'listeCat.html')
def reservation(request):
    return render(request, 'reservation.html')
def modifier(request):
    return render(request, 'modifier.html')
def utilisateur(request):
    return render(request, 'utilisateur.html')
def visite(request):
    return render(request, 'visite.html')
def listeVente(request):
    return render(request, 'listeVente.html')