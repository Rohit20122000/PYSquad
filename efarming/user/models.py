from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age =  models.IntegerField()
    address = models.TextField()
    contact = models.IntegerField()
    

    def __str__(self):
        return self.user_name

    
class Vendor(models.Model):
    vendor_data = models.ForeignKey(User,on_delete=models.CASCADE)
    Area_code= models.CharField(max_length=100)

    def __str__(self):
        return self.Area_code

class Customer(models.Model):
    customer_data = models.ForeignKey(User,on_delete=models.CASCADE)
    Pin = models.CharField(max_length=100)

    def __str__(self):
        return self.Pin