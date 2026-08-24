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
    return Response(serializer.errors,status=400)

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
    except Exception as e:
            return Response({"error": str(e)}, status=500)

    possessions = Possessions.objects.filter(user=user)
    serializer = PossessionSerializer(possessions, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updatepossessions(request, user_id):
    try:
        user=Users.objects.get(id=user_id)
        print(f'userfound{user}')
        if not user:
            return Response({'message':'User not found'})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
    itemId=request.data.get('id')
    try:
        possessions=Possessions.objects.get(user=user,id=itemId)
        print(f'possession found{possessions}')
        serializer=PossessionSerializer(possessions, data=request.data)
        print(f'serializer{possessions}')

        if serializer.is_valid():
            print(f'serializer is valid')
            serializer.save()
            return Response({"message":"possession updated successfully", 
                            "data":serializer.data})
        return Response(serializer.errors)
    except Exception as e:
            return Response({"error": str(e)}, status=500)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
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
    return Response(serializer.errors,status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def gettasks(request, user_id):
    try:
        user = Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        return Response(
            {'message': 'User not found'},
            status=404
        )
    tasks=Tasks.objects.filter(user=user)
    serializer=TaskSerializer(tasks, many=True)
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