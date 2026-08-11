from .views import *
from django.urls import path

urlpatterns=[
    #possessions
    path('addpossessions/<int:user_id>/',addpossessions,name ='addpossessions'),
    path('getpossessions/<int:user_id>/',getpossessions,name='getpossessions'),
    path('updatepossessions/<int:user_id>/',updatepossessions,name='updatepossessions'),
    path('deletepossession/<int:user_id>/',deletepossession, name='deletepossession'),

    #tasks
    path('addtasks/<int:user_id>/', addtasks,name='addtasks'),
    path('gettasks/<int:user_id>/',gettasks,name='gettasks'),
    path('updatetasks/<int:user_id>/',updatetasks,name='updatetasks'),
    path('deletetasks/<int:user_id>/',deletetasks,name='deletetasks'),

    #Checkins
    path('addcheckin/<int:user_id>/', addcheckin,name='addcheckin'),
    path('getcheckin/<int:user_id>/',getcheckin,name='getcheckin'),
    path('updatecheckin/<int:user_id>/',updatecheckin,name='updatecheckin'),
    path('deletecheckin/<int:user_id>/',deletecheckin,name='deletecheckin'),
]