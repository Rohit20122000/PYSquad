from django.shortcuts import render
from .forms import  ProductForm
# Create your views here.

def product_view(request):
    
    form = ProductForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "productform.html",{'form':form})