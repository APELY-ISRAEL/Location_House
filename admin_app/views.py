from pyexpat.errors import messages
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model

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

def edit_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    return render(request, 'modifierCat.html', {'categorie': categorie})

def modifier_categorie(request, categorie_id):
    if request.method == 'POST':
        libelle = request.POST['libelle']
        categorie = get_object_or_404(Categorie, id=categorie_id)
        categorie.libelle = libelle  # Mettre à jour le libellé de la catégorie
        categorie.save()
        return redirect('listeCat')  # Rediriger vers la liste des catégories après modification
    else:
        return redirect('modifierCat', categorie_id=categorie_id)  # Rediriger vers la page de modification


def liste(request):
    # Récupérer toutes les maisons depuis la base de données
    maisons = Maison.objects.all()
    context = {'maisons': maisons}
    return render(request, 'liste.html', context)

def listeCat(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'listeCat.html', context)

def delete_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('listeCat')  # Rediriger vers une vue appropriée après la suppression
    return render(request, 'listeCat.html', {'categorie': categorie})
    

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

def delete_user(request, user_id):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    # Rediriger vers la vue des utilisateurs après la suppression
    return redirect('utilisateur')

def modify_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        new_role = request.POST.get('role')
        user.role = new_role
        user.save()
        return redirect('utilisateur')
    return render(request, 'utilisateur.html', {'utilisateur': user})

def modifier_maison(request, maison_id):
    maison = get_object_or_404(Maison, id=maison_id)
    categories = Categorie.objects.all()  # Récupérer toutes les catégories
    context = {'maison': maison, 'categories': categories}
    return render(request, 'modifier.html', context)

def edit_maison(request, maison_id):
    maison = get_object_or_404(Maison, id=maison_id)
    if request.method == 'POST':
        # Modifier les attributs de la maison selon les données reçues dans la requête POST
        maison.titre = request.POST.get('titre')
        maison.description = request.POST.get('description')
        maison.adresse = request.POST.get('adresse')
        maison.categorie_id = request.POST.get('categorie')
        maison.prix = request.POST.get('prix')
        maison.statut = request.POST.get('statut')
        # Enregistrer les modifications
        maison.save()
        return redirect('liste')  # Rediriger vers la liste des maisons après la modification
    return render(request, 'modifier.html', {'maison': maison})

def delete_maison(request, maison_id):
    maison = get_object_or_404(Maison, id=maison_id)
    if request.method == 'POST':
        maison.delete()
        return redirect('liste')  # Rediriger vers la liste des maisons après la suppression
    return render(request, 'liste.html', {'maison': maison})
   
