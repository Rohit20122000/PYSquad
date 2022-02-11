from django.db import models

# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age =  models.IntegerField()
    address = models.TextField()
    contact = models.IntegerField()

    def __str__(self):
        return self.user_name

    
class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name