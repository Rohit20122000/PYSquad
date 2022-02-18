from django.contrib import admin

# Register your models here.
from .models import ProductType,Catagory,warehouse,VendorInventory

class VendorInventoryAdmin(admin.ModelAdmin):
    list_display = ('vendor','productname','acceptbutton','deniedbutton')

    def save_model(self, request, obj, form, change):
        if obj.acceptbutton:
            if not warehouse.objects.filter(order=obj).exists():
                warehouse.objects.create(order=obj, areaname="A")
        elif not obj.acceptbutton and warehouse.objects.filter(order=obj).exists():
            warehouse.objects.filter(order=obj).first().delete()

        aa = super(VendorInventoryAdmin, self).save_model(request, obj, form, change)
        return aa


admin.site.register(ProductType)
admin.site.register(Catagory)
admin.site.register(warehouse)
admin.site.register(VendorInventory,VendorInventoryAdmin)