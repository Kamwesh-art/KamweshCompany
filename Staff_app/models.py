from django.db import models
from django.conf import settings 

# Create your models here.
class Possessions(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    serialno=models.CharField(max_length=700)
    item=models.CharField(max_length=255)
    quantity=models.IntegerField(blank=True,null=True)
    cost=models.DecimalField(max_digits=1000,decimal_places=2)

    def __str__(self):
        return self.item

class Tasks(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    task=models.CharField(max_length=70)
    description=models.CharField(max_length=255)
    ETA=models.DateTimeField()
    is_done=models.BooleanField(default=False)

    def __str__(self):
        return self.task


class Checkin(models.Model): 
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date=models.DateField()
    arrival_time= models.TimeField()
    depature_time= models.TimeField()

    def __str__(self):
        return str(self.user.username)


