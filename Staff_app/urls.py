from .views import *
from django.urls import path

urlpatterns=[
    path('addpossessions/<int:user_id>/',addposessions,name ='addpossessions'),
    path('getpossessions/<int:user_id>/',getpossessions,name='getpossessions'),
    path('deletepossession/<int:user_id>/',deletepossession, name='deletepossession'),
    path('addtask/<int:user_id>/', addtask,name="addtask"),
]