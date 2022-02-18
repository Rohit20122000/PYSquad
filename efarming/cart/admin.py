from django.contrib import admin

# Register your models here.
from .models import Order,Cart

admin.site.register(Order)
admin.site.register(Cart)

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)