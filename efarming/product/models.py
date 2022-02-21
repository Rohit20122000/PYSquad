from django.db import models

from warehouse.models import Warehouse

# Create your models here.
class Product(models.Model):
    product_name = models.ForeignKey(Warehouse,on_delete=models.CASCADE)
    price = models.IntegerField(help_text="Per Kg")
    description = models.TextField()
   # product_quntity = models.IntegerField(help_text="In Kg")

    def __str__(self):
        return  f"{self.product_name }"