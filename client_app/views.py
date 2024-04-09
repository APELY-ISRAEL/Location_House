from django.shortcuts import render
from .models import Client



def home(request):
        return render(request, 'home.html')
   
def house(request):
    return render(request, 'house.html')

def contact(request):
    return render(request, 'contact.html')

def category(request):
    return render(request, 'category.html')