
import imp
from django.db import models
from user.models import Customer
from product.models import Product
from user.models import User

# Create your models here.


class Cart(models.Model):
    customer_name = models.ForeignKey(Customer,on_delete=models.CASCADE) 
    product = models.ManyToManyField(Product)
    add_date = models.DateField(null=True,blank=True)
    product_quantity = models.TextField()
    is_ordered = models.BooleanField("Confirm",default=False,max_length=50)

    def __str__(self) -> str:
        return f"{self.customer_name}"

class Order(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    address = models.TextField()
    details = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    delivery_date = models.DateField()
    product_quntity = models.IntegerField()
   

    def __str__(self) -> str:
        return f"{self.cart.customer_name}"
