from django.db import models

# Create your models here.

class warehouse(models.Model):
    areaCode= models.UUIDField(primary_key=True)
    stoke = models.IntegerField(max_length=100)
    capacity = models.IntegerField(max_length=100)
    no_of_vehicles = models.IntegerField(max_length=100)
    

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
    description = models.TextField()

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
