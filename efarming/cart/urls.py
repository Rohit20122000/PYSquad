from django.urls import path
from . import views

urlpatterns = [
    path('order', views.order_view),
    path('cart',views.cart_view),
]