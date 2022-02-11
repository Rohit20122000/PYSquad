from django.db import models

# Create your models here.

class warehouse(models.Model):
    areaCode= models.UUIDField(primary_key=True)
    stoke = models.IntegerField()
    capacity = models.IntegerField()
    no_of_vehicles = models.IntegerField()
    

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    catagory_name=models.CharField(max_length=100)
    description = models.TextField()

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    
