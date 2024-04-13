from django.urls import include, path
from auth_app import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login1, name='login'),
    path('logout/', views.logout1, name='logout'),
    
    
]