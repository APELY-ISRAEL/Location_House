
from django.contrib import admin
from django.urls import include, path
from admin_app import views
from client_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_app/', include('auth_app.urls')),
    path('client_app/', include('client_app.urls')),
    path('admin_app/', include('admin_app.urls')),
    path('', views.home, name='home'),
   
    
    
]
