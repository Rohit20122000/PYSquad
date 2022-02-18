from django.db import models

# Create your models here.

class Cart(models.Model):
    customer_name = models.CharField(max_length=50)   
    no_of_product = models.IntegerField()
    add_date = models.DateField(null=True,blank=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return self.customer_name

class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    address = models.TextField()
    details = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    delivery_date = models.DateField()
    product_quntity = models.IntegerField()

    def __str__(self) -> str:
        return self.price
