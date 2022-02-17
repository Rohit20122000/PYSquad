from django.contrib import admin

# Register your models here.
from .models import ProductType,Catagory,warehouse,VendorInventory

admin.site.register(ProductType)
admin.site.register(Catagory)
admin.site.register(warehouse)
admin.site.register(VendorInventory)

