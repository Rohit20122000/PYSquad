from django.contrib import admin

# Register your models here.
from .models import Vendor,Customre,user

admin.site.register(Vendor)
admin.site.register(Customre)
admin.site.register(user)