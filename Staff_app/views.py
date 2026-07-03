from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
#adding possessions
@api_view(['POST'])
def addposessions(request,user_id):
    data= request.data.copy()
    data["user"]= user_id
    serializer=PossessionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

#getting possessions
@api_view(['GET'])
def getpossessions(request,user_id):
    possessions=Possessions.objects.filter(user_id=user_id)
    serializer=PossessionSerializer(possessions, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deletepossession(request, user_id):
    possession= Possessions.objects.get(id=pk)
    possession.delete()

    return Response({"message":"Possession has been deleted."})