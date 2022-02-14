from django.db import models

# Create your models here.

Catagory_Choices = (("FRUIT","FRUIT"),
                  ("VAGETABLE","VAGETABLE"))
Subcat_Choices = (("potato","potato"),("tomato","tomato"),("onion","onion"),
                  ("apple","apple"),("banana","banana"))


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

class VendorInventory(models.Model):
    product_name = models.CharField(max_length=100)
    Date_for_ready = models.DateField()
    your_price_perKG = models.IntegerField()
    Catagory = models.CharField(choices=Catagory_Choices,max_length=50)
    Sub_Catagory = models.CharField(choices=Subcat_Choices,max_length=50)

    
    def __str__(self):
        return self.product_name
    
   