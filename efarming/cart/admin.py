from django.contrib import admin

# Register your models here.
from .models import Order,Cart
from product.models import Product
from user.models import User

class CartAdmin(admin.ModelAdmin):
    list_display = ('customer_name',)

    @staticmethod
    def generate_price(product_str=None):
        if not product_str:
            return 0
        products = product_str.split(',')
        price = 0
        for product in products:
            product_detail = product.split(":")
            product = Product.objects.filter(product_name__order__product_name=product_detail[0]).first()
            if product:
                price += int(product.price) * int(product_detail[1])
        return price
    
    def save_model(self, request, obj, form, change):
        if obj.is_ordered:
            if not Order.objects.filter(cart=obj).first():
                Order.objects.create(cart=obj, address=obj.customer_name.customer_data.address, details="Product.description", price=self.generate_price(product_str=obj.product_quantity) ,delivery_date=obj.add_date.replace(day=obj.add_date.day+1), product_quntity=len(obj.product.all()))
            else:
                order = Order.objects.filter(cart=obj).first()
                order.price = self.generate_price(obj.product_quantity)
                order.product_quntity = len(obj.product.all())
                order.save()
        elif not obj.is_ordered and Order.objects.filter(cart=obj).first():
            Order.objects.filter(cart=obj).first().delete()


        cart_super = super(CartAdmin, self).save_model(request, obj, form, change)
        return cart_super




admin.site.register(Order)
admin.site.register(Cart,CartAdmin)

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)