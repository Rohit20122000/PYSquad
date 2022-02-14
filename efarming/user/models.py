from django.db import models

"""USER_CHOICES = (("Vendor","Vendor"),("Customer","Customer"))"""

# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=100)
    Vendor = models.ForeignKey(max_length=50,on_delete=models.CASCADE)
    user_password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age =  models.IntegerField()
    address = models.TextField()
    contact = models.IntegerField()
"""    user_field = models.CharField(choices=USER_CHOICES,max_length=8)"""


    
class Vendor(models.Model):
    code = models.IntegerField()



class Customer(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age =  models.IntegerField()
    address = models.TextField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name