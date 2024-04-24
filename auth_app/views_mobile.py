# serializers.py
from rest_framework import serializers
from auth_app.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role')  # Ajoutez d'autres champs si nécessaire

# views.py
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from auth_app.models import CustomUser
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login1(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response({'message': 'Votre compte est inactif.'}, status=400)
        else:
            return Response({'message': 'Nom d\'utilisateur ou mot de passe incorrect.'}, status=400)

@api_view(['GET'])
def logout1(request):
    logout(request)
    return Response({'message': 'Vous êtes déconnecté.'}, status=200)