from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)
    email = models.CharField(unique=True,max_length=100)
    age =  models.IntegerField()
    address = models.TextField()
    contact = models.IntegerField()
    

    def __str__(self):
        return f"{self.user_name}"

    
class Vendor(models.Model):
    
    vendor_data = models.ForeignKey(User,on_delete=models.CASCADE)
    area_code= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vendor_data.user_name}" 

class Customer(models.Model):
    customer_data = models.ForeignKey(User,on_delete=models.CASCADE)
    pin = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_data}"