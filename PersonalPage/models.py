from django.db import models
# Create your models here.

class User_Recording_Sell(models.Model):
    artist = models.ForeignKey('Artist' , on_delete=models.SET_NULL , null=True)
    recording = models.ForeignKey('Recording' , on_delete=models.SET_NULL , null=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_length=15)
    user = models.ForeignKey('User', on_delete=models.SET_NULL() , null=True)
