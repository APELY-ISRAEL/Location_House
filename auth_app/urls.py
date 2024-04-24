from django.urls import include, path
from auth_app import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login1, name='login'),
    path('logout/', views.logout1, name='logout'),
    path('register1/', views.register1, name='register1'),
    path('login2/', views.login2, name='login2'),
    path('logout2/', views.logout2, name='logout2'),
]
