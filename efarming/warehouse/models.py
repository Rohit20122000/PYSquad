from cProfile import label
from django.db import models
from user.models import Vendor
# Create your models here.

CATAGORY_CHOICES = (("FRUIT","FRUIT"),
                  ("VAGETABLE","VAGETABLE"))
                  
SUBCAT_CHOICES = (("potato","potato"),("tomato","tomato"),("onion","onion"),
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
    product_name = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    date_for_ready = models.DateField()
    catagory = models.CharField(choices=CATAGORY_CHOICES,max_length=50)
    subcatagory = models.CharField(choices=SUBCAT_CHOICES,max_length=50)
    sell_price = models.IntegerField(help_text="price per Kg")
    is_accept = models.BooleanField("Accept",default=False,max_length=50)
    
    def __str__(self):
        return f"{self.vendor.vendor_data}"


class Warehouse(models.Model):
    order = models.OneToOneField(VendorInventory,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.order.productname}"
