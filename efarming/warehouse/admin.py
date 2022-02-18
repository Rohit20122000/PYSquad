from django.contrib import admin

# Register your models here.
from .models import ProductType,Catagory,Warehouse,VendorInventory


class VendorInventoryAdmin(admin.ModelAdmin):
    list_display = ('vendor','product_name','sell_price','is_accept')

    def save_model(self, request, obj, form, change):
        if obj.is_accept:
            if not Warehouse.objects.filter(order=obj).exists():
                Warehouse.objects.create(order=obj,procuct_price = False ,is_ready=False)
        elif not obj.is_accept and Warehouse.objects.filter(order=obj).exists():
            Warehouse.objects.filter(order=obj).first().delete()

        vendor_super = super(VendorInventoryAdmin, self).save_model(request, obj, form, change)
        return vendor_super



class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('order','procuct_price','is_ready')
    

admin.site.register(ProductType)
admin.site.register(Catagory)
admin.site.register(Warehouse,WarehouseAdmin)
admin.site.register(VendorInventory,VendorInventoryAdmin)