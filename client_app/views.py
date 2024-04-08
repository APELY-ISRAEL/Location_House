from django.shortcuts import render
from .models import Client

def home(request):
    clients = Client.objects.all()
    return render(request, 'home.html', {'clients': clients})