from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Possesions(models.Model):
    seriviceid=models.CharField(max_length=700)
    item=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255, blank=True,null=True)
    cost=models.CharField(max_length=255)

class tasks(models.Model):
    {

    }
class Checkin(models.Model): 
    {

    }   

