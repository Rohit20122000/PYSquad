from codecs import backslashreplace_errors
from operator import mod
from django.db import models

# Create your models here.
class Order(models.Model):
    address = models.TextField()
    details = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    deliveryDate = models.DateField()
    productQuntity = models.IntegerField()

class Cart(models.Model):
    no_of_product = models.IntegerField()
    add_date = models.DateField(null=True,blank=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)