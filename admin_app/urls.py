from django.urls import path
from admin_app import views


urlpatterns = [
    path('index/', views.index, name='index'),
     path('ajout/', views.ajout, name='ajout'),
     path('categorie/', views.categorie, name='categorie'),
     path('liste/', views.liste, name='liste'),
      path('listeVente/', views.listeVente, name='listeVente'),
     path('listeCat/', views.listeCat, name='listeCat'),
     path('modifier/', views.modifier, name='modifier'),
     path('reservation/', views.reservation, name='reservation'),
     path('utilisateur/', views.utilisateur, name='utilisateur'),
      path('visite/', views.visite, name='visite'),
     
]
