from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    phone=models.CharField(max_length=255, blank=True, null=True)
    department=models.CharField(max_length=255)

