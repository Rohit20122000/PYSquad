from django.db import models

# Create your models here.

Product_Choices = (("FRUIT","FRUIT"),
                  ("VAGETABLE","VAGETABLE"))

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
    your_price = models.IntegerField()
    product_type = models.CharField(choices=Product_Choices,max_length=50)

    
    def __str__(self):
        return self.product_name
    
    """
    product_type = models.CharField(max_length = 20,
    choices = Product_Choices)"""