from django.urls import path
from . import views

urlpatterns = [
    path('producttype', views.producttype_view),
    path('warehouse', views.warehouse_view),
    path('catagory', views.catagory_view),
    path('Inventoryform',views.Inventory_view),
    
]