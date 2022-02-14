import imp
from django.shortcuts import render
from .forms import OrderForm,CartForm
# Create your views here.


def  order_view(request):
    form = OrderForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request,"cartform.html",{'form':form})

def  cart_view(request):
    form = CartForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request,"cartform.html",{'form':form})