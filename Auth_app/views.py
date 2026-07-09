from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from django.contrib.auth import authenticate
from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer_class= RegisterSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data)
    return Response ({"message":"Provide the required details"})

@api_view(['POST'])
def login(request):
    serializer= LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username=serializer.validated_data['username']
    password=serializer.validated_data['password']

    user= authenticate(
        username =username,
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