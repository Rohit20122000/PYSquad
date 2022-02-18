from django.db import models

from warehouse.models import Warehouse

# Create your models here.
class Product(models.Model):
    product_name = models.ForeignKey(Warehouse,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    product_quntity = models.IntegerField()

    def __str__(self):
        return  self.name