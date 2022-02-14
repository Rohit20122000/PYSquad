from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    productQuntity = models.IntegerField()

    def __str__(self):
        return  self.name