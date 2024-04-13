from django.urls import path
from client_app import views


urlpatterns = [
     path('home/', views.home, name='home'),
       path('house/', views.house, name='house'),
        path('contact/', views.contact, name='contact'),
         path('category/', views.category, name='category'),
          path('profil/', views.profil, name='profil'),
   
]