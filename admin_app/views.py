from pyexpat.errors import messages
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User

 

# Create your views here.


# Dans views.py de votre application (client_app, admin_app, etc.)

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from auth_app.models import CustomUser

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

        # Vérifier si un fichier a été téléchargé
        if photo:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Utilisation de MEDIA_ROOT
            filename = fs.save(photo.name, photo)
            photo_url = fs.url(filename)
        else:
            photo_url = None

        # Créer une nouvelle instance de Maison avec les données du formulaire
        nouvelle_maison = Maison(titre=titre, description=description, adresse=adresse,
                                 categorie_id=categorie_id, prix=prix, statut=statut, photo=photo_url)
        # Enregistrer la nouvelle maison dans la base de données
        nouvelle_maison.save()

        # Rediriger vers une page de confirmation ou une autre vue
        return redirect('liste')  # Rediriger vers la vue de détail de la maison par exemple

    # Si la méthode de requête n'est pas POST, afficher le formulaire
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'ajout.html', context)

def categorie(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        libelle = request.POST.get('libelle')

        # Créer une nouvelle instance de Categorie avec les données du formulaire
        nouvelle_categorie = Categorie(libelle=libelle)
        # Enregistrer la nouvelle catégorie dans la base de données
        nouvelle_categorie.save()

        # Rediriger vers une page de confirmation ou une autre vue
        return redirect('listeCat')  # Rediriger vers la même page après l'enregistrement
    # Si la méthode de requête n'est pas POST, afficher le formulaire
    
    return render(request, 'categorie.html')

def liste(request):
    # Récupérer toutes les maisons depuis la base de données
    maisons = Maison.objects.all()
    context = {'maisons': maisons}
    return render(request, 'liste.html', context)

def listeCat(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'listeCat.html', context)

def sup_categorie(request, categorie_id):
    if request.method == 'POST':
        categorie = Categorie.objects.get(pk=categorie_id)
        categorie.delete()
        messages.success(request, 'Catégorie supprimée avec succès.')
        return redirect('listeCat')
    else:
        messages.error(request, 'Erreur lors de la suppression de la catégorie.')
        return redirect('listeCat')
    

def reservation(request):
    return render(request, 'reservation.html')
def modifier(request):
    return render(request, 'modifier.html')

def utilisateur(request):
    utilisateurs = CustomUser.objects.all()
    context = {'utilisateurs': utilisateurs}
    return render(request, 'utilisateur.html', context)

def visite(request):
    return render(request, 'visite.html')
def listeVente(request):
    return render(request, 'listeVente.html')