from django.db import models
from auth_app.models import User 
# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=255)
    
    def __str__(self):
        return self.libelle


class Maison(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='C:/Users/israe/Documents', blank=True, null=True)

    
    def __str__(self):
        return self.titre


class Reservation(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=50)
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Visite(models.Model):
    email = models.EmailField()
    lieux = models.CharField(max_length=255)
    date_arrivee = models.DateField()
    telephone = models.CharField(max_length=15)
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email
