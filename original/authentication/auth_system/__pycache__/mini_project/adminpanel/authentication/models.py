from django.db import models


# Create your models here.

class Puma(models.Model):
    name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'images')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False) 
