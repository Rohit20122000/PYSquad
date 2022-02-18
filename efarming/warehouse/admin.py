from django.contrib import admin

# Register your models here.
from .models import ProductType,Catagory,Warehouse,VendorInventory

class VendorInventoryAdmin(admin.ModelAdmin):
    list_display = ('vendor','product_name','sell_price','is_accept')

    def save_model(self, request, obj, form, change):
        if obj.is_accept:
            if not Warehouse.objects.filter(order=obj).exists():
                Warehouse.objects.create(order=obj)
        elif not obj.is_accept and Warehouse.objects.filter(order=obj).exists():
            Warehouse.objects.filter(order=obj).first().delete()

        aa = super(VendorInventoryAdmin, self).save_model(request, obj, form, change)
        return aa


admin.site.register(ProductType)
admin.site.register(Catagory)
admin.site.register(Warehouse)
admin.site.register(VendorInventory,VendorInventoryAdmin)