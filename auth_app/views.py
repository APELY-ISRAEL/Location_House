from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from auth_app.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from auth_app.models import CustomUser
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
def register(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = 'client'  # Par défaut, nouvel utilisateur est un client

        # Créer un nouvel utilisateur
        user = CustomUser.objects.create_user(username=username, email=email, password=password, role=role)

        # Rediriger vers la page de connexion après l'inscription réussie
        return redirect('login')

    return render(request, 'register.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Vérifier si l'utilisateur existe dans la base de données
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:  # Vérifier si le compte est actif
                login(request, user)
                # Rediriger l'utilisateur vers la page appropriée
                if user.role == 'admin':
                    return redirect('index')
                elif user.role == 'client':
                    return redirect('home')
            else:
                # Compte inactif, afficher un message d'erreur
                messages.error(request, 'Votre compte est inactif.')
                return redirect('login')  # Redirection vers la page de connexion
        else:
            # Informer l'utilisateur que les informations de connexion sont incorrectes
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return redirect('login')  # Redirection vers la page de connexion

    return render(request, 'login.html')

def logout1(request):
    logout(request)
    return redirect('login')



# serializers.py
from rest_framework import serializers
from auth_app.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')  # Ajoutez d'autres champs si nécessaire

# views.py


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return get_user_model().objects.create(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

@api_view(['POST'])
@permission_classes([AllowAny])
def register1(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login2(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Nom d\'utilisateur et mot de passe requis'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    if not user:
        return Response({'error': 'Nom d\'utilisateur ou mot de passe incorrect'}, status=status.HTTP_400_BAD_REQUEST)

    if not user.is_active:
        return Response({'error': 'Compte désactivé'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=status.HTTP_200_OK)

@api_view(['GET'])
def logout2(request):
    logout(request)
    return Response({'message': 'Vous êtes déconnecté.'}, status=200)






