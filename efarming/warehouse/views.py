from django.shortcuts import render
from .forms import ProductTypefForm,WarehouseForm,CatagoryForm

# Create your views here.
def producttype_view(request):
 
    form = ProductTypefForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "warehouseform.html",{'form':form})

def warehouse_view(request):
 
    form = WarehouseForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "warehouseform.html",{'form':form})

def catagory_view(request):
 
    form = CatagoryForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "warehouseform.html",{'form':form})

