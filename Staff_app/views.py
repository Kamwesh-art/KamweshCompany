from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Auth_app.models import Users


# Create your views here.
#possessions
# adding possessions
@api_view(['POST'])
def addpossessions(request,user_id):
    data= request.data.copy()
    data["user"]= user_id
    serializer=PossessionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def addpossessions(request):
#     data = request.data.copy()
#     data["user"] = request.user.id
#     serializer = PossessionSerializer(data=data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# #getting possessions
# @api_view(['GET'])
# def getpossessions(request,user_id):
#     possessions=Possessions.objects.filter(user=request.user)
#     serializer=PossessionSerializer(possessions, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getpossessions(request,user_id):
    try:
        user=Users.objects.get(id=user_id)
        if not user:
            return Response({'message':'User not found'})
    except:
        pass

    possessions = Possessions.objects.filter(user=user)
    serializer = PossessionSerializer(possessions, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updatepossessions(request, user_id):
    possessions=Possessions.objects.get(id=user_id)
    serializer=PossessionSerializer(possessions, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"pOsssession updated successfully", 
                         "data":serializer.data})

@api_view(['DELETE'])
def deletepossession(request, user_id):
    possession= Possessions.objects.get(id=user_id)
    possession.delete()

    return Response({"message":"Possession has been deleted."})

# #tasks
@api_view(['POST'])
def addtasks(request,user_id):
    data=request.data.copy()
    data["user"]=user_id
    serializer=TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def gettasks(request, user_id):
    task=Tasks.objects.filter(user_id=user_id)
    serializer=TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updatetasks(request, user_id):
    task= Tasks.objects.get(id=user_id)
    serializer=TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Task has been updated successfully.",
                         "data":serializer.data})

@api_view(['DELETE'])
def deletetasks(request,user_id):
    task=Tasks.objects.get(id=user_id)
    task.delete()

    return Response({"message":"Task assigned deleted."})
    
#Checkins
@api_view(['POST'])
def addcheckin(request, user_id):
    data=request.data.copy()
    data["user"]=user_id
    serializer=CheckinSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def getcheckin(request, user_id):
    checkin=Checkin.objects.filter(user_id=user_id)
    serializer=CheckinSerializer(checkin, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updatecheckin(request,user_id):
    checkin=Checkin.objects.get(id=user_id)
    serializer=CheckinSerializer(checkin,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Checkin updates done",
                         "data": serializer.data})

@api_view(['DELETE'])
def deletecheckin(request,user_id):
    checkin=Checkin.objects.get(id=user_id)
    checkin.delete()
    return Response({"message":"Checkin deleted."})