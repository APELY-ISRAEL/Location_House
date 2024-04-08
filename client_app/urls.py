from django.urls import path
from client_app import views


urlpatterns = [
     path('home/', views.home, name='home'),
   
]