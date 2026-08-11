from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer= RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST
)

@api_view(['POST'])
def login(request):
    serializer= LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    emailUsername =serializer.validated_data['username']
    password =serializer.validated_data['password']

    # Find the user by either email or username
    if '@' in emailUsername:
        user = Users.objects.filter(email=emailUsername).first()
    else:
        user = Users.objects.filter(username=emailUsername).first()

    if user is None:
        return Response(
            {"message": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Authenticate using the username
    user = authenticate(
        username=user.username,
        password=password
    )

    if user is None:
        return Response({"message":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
    
    refresh= RefreshToken.for_user(user)
    
    return Response(
        {
         "username":user.username,
         "refresh": str(refresh),
         "access": str(refresh.access_token)
         }
    )

@api_view(['POST'])
def logout(request):
    logout (request)
    return Response({"message":"User Logged out successfully "})