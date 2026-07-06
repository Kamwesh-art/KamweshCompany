from .views import *
from django.urls import path

urlpatterns=[
    path('addpossessions/<int:user_id>/',addposessions,name ='addpossessions'),
    path('getpossessions/<int:user_id>/',getpossessions,name='getpossessions'),
    path('deletepossession/<int:user_id>/',deletepossession, name='deletepossession'),
    path('addtasks/<int:user_id>/', addtasks,name="addtask"),
    path('gettasks/<int:user_id>/',gettasks,name='gettask'),
]