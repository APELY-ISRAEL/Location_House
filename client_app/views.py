from django.shortcuts import render
from .models import Client
from django.contrib.auth.decorators import login_required


def home(request):
    clients = Client.objects.all()
    return render(request, 'home.html', {'clients': clients})

def house(request):
    return render(request, 'house.html')

def contact(request):
    return render(request, 'contact.html')

def category(request):
    return render(request, 'category.html')