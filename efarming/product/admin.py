from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_quntity','price')
    def has_add_permission(self, request):
        return False


admin.site.register(Product,ProductAdmin)

