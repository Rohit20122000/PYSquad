from django.contrib import admin


# Register your models here.
from .models import ProductType,Catagory,Warehouse,VendorInventory
from product.models import Product



class VendorInventoryAdmin(admin.ModelAdmin):
    list_display = ('vendor','product_name','sell_price','is_accept')

    def has_add_permission(self, request):
        return False

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
    
    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        if obj.is_ready:
            if not Product.objects.filter(product_name=obj).exists():
                Product.objects.create(product_name=obj,name = False ,price=False,description = False,product_quntity = False)
        elif not obj.is_ready and Product.objects.filter(product_name=obj).exists():
            Product.objects.filter(product_name=obj).first().delete()

        vendor_super = super(WarehouseAdmin, self).save_model(request, obj, form, change)
        return vendor_super

admin.site.register(ProductType)
admin.site.register(Catagory)
admin.site.register(Warehouse,WarehouseAdmin)
admin.site.register(VendorInventory,VendorInventoryAdmin)