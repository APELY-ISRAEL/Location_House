
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from admin_app import views
from client_app import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_app/', include('auth_app.urls')),
    path('client_app/', include('client_app.urls')),
    path('admin_app/', include('admin_app.urls')),
    path('', views.home, name='home'),   
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)