
from django.urls import path
from . import views

urlpatterns = [
    path('vendor', views.vendor_view),
    path('user', views.user_view),
    path('customer', views.customer_view)
]