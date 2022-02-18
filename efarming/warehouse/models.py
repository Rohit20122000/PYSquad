from django.db import models
from user.models import Vendor
# Create your models here.

Catagory_Choices = (("FRUIT","FRUIT"),
                  ("VAGETABLE","VAGETABLE"))
Subcat_Choices = (("potato","potato"),("tomato","tomato"),("onion","onion"),
                  ("apple","apple"),("banana","banana"))
                  

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
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    productname = models.CharField(max_length=100)
    ProductQuantity = models.IntegerField()
    Dateforready = models.DateField()
    Catagory = models.CharField(choices=Catagory_Choices,max_length=50)
    SubCatagory = models.CharField(choices=Subcat_Choices,max_length=50)
    acceptbutton = models.BooleanField("Accept",default=False,max_length=50)
    deniedbutton = models.BooleanField("Denied",default=False,max_length=50)
    
    

    
    def __str__(self):
        return f"{self.vendor.vendor_data}"

class warehouse(models.Model):
    order = models.ForeignKey(VendorInventory,on_delete=models.CASCADE)
    areaname=models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.order.productname}"