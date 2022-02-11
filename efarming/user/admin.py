from django.contrib import admin

# Register your models here.
from .models import Vendor,Customer,user

admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(user)