from .views import *
from django.urls import path

urlpatterns=[
    path('addpossessions/<int:user_id>/',addposessions,name ='addpossessions'),
    path('getpossessions/<int:user_id>/',getpossessions,name='getpossessions'),
]