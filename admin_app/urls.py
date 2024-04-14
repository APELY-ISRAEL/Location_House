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
     path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
      path('modifier_role/<int:user_id>/', views.modify_role, name='modify_role'),
     path('delete_categorie/<int:categorie_id>/', views.delete_categorie, name='delete_categorie'),
     path('edit_categorie/<int:categorie_id>/', views.edit_categorie, name='edit_categorie'),
     path('modifier_categorie/<int:categorie_id>/', views.modifier_categorie, name='modifier_categorie'),
     path('maison/modifier/<int:maison_id>/', views.modifier_maison, name='modifier_maison'),
      path('edit_maison/<int:maison_id>/', views.edit_maison, name='edit_maison'),
    path('delete_maison/<int:maison_id>/', views.delete_maison, name='delete_maison'),


     
]
