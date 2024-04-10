from django.urls import path
from admin_app import views


urlpatterns = [
    path('index/', views.index, name='index'),
     path('ajout/', views.ajout, name='ajout'),
    
     
   
]