from django.contrib import admin

# Register your models here.
from .models import ProductType,Catagory,warehouse,VendorInventory

class VendorInventoryAdmin(admin.ModelAdmin):
    list_display = ('vendor','productname','acceptbutton','deniedbutton')

admin.site.register(ProductType)
admin.site.register(Catagory)
admin.site.register(warehouse)
admin.site.register(VendorInventory,VendorInventoryAdmin)