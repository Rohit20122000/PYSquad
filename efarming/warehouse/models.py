from django.db import models

# Create your models here.

class warehouse(models.Model):
    areaCode= models.UUIDField(primary_key=True)
    stoke = models.IntegerField()
    capacity = models.IntegerField()
    no_of_vehicles = models.IntegerField()

    def __str__(self):
        return self.stoke

    

class ProductType(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    catagory_name=models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name


class Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

    
