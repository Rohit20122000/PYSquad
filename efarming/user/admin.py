from django.contrib import admin

# Register your models here.
from .models import Vendor,Customer,User

admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(User)