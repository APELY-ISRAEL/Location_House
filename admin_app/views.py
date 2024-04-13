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
from django.shortcuts import render, redirect
from .models import Categorie, Maison  # Assurez-vous d'importer votre modèle Maison

def ajout(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        adresse = request.POST.get('adresse')
        categorie_id = request.POST.get('categorie')
        prix = request.POST.get('prix')
        statut = request.POST.get('statut')
        photo = request.FILES.get('photo')  # Assurez-vous d'avoir enctype="multipart/form-data" dans votre formulaire

        # Créer une nouvelle instance de Maison avec les données du formulaire
        nouvelle_maison = Maison(titre=titre, description=description, adresse=adresse,
                                 categorie_id=categorie_id, prix=prix, statut=statut, photo=photo)
        # Enregistrer la nouvelle maison dans la base de données
        nouvelle_maison.save()

        # Rediriger vers une page de confirmation ou une autre vue
        return redirect('ajout', id=nouvelle_maison.id)  # Rediriger vers la vue de détail de la maison par exemple

    # Si la méthode de requête n'est pas POST, afficher le formulaire
    return render(request, 'ajout.html')

def categorie(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        libelle = request.POST.get('libelle')

        # Créer une nouvelle instance de Categorie avec les données du formulaire
        nouvelle_categorie = Categorie(libelle=libelle)
        # Enregistrer la nouvelle catégorie dans la base de données
        nouvelle_categorie.save()

        # Rediriger vers une page de confirmation ou une autre vue
        return redirect('categorie', id=nouvelle_categorie.id)  # Rediriger vers la vue de détail de la catégorie par exemple
     
    # Si la méthode de requête n'est pas POST, afficher le formulaire
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