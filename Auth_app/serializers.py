from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True)
    
    class Meta:
        model= Users
        fields='__all__'

    def create(self, validated_data):
        user= Users.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
