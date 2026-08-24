from .models import *
from rest_framework import serializers 

class PossessionSerializer(serializers.ModelSerializer):
   class Meta:
        model =Possessions
        fields='__all__'
        # read_only_fields = ['user']

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
        model=Tasks
        fields='__all__'
        # read_only_fields = ['user']

class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model=Checkin
        fields='__all__'
        read_only_fields = ['user']