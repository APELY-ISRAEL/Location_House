from django.shortcuts import render

 

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Dans views.py de votre application (client_app, admin_app, etc.)

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def hone(request):
    if request.user.is_authenticated:
        if request.user.role == 'admin' and request.user.admin_id == '12345678':
            return redirect('index')
        elif request.user.role == 'client':
            return redirect('home')
    return redirect('login')

# Autres vues comme client_dashboard, admin_dashboard, etc.
def ajout(request):
    return render(request, 'ajout.html')