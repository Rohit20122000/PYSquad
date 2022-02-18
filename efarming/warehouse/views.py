from django.shortcuts import render
from .forms import ProductTypefForm,WarehouseForm,CatagoryForm,InventoryForm

# Create your views here.
def producttype_view(request):
 
    form = ProductTypefForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "productform.html",{'form':form})

def warehouse_view(request):
 
    form = WarehouseForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "warehouseform.html",{'form':form})

def catagory_view(request):
 
    form = CatagoryForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "catagoryform.html",{'form':form})

def Inventory_view(request):
 
    form = InventoryForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "warehouseform.html",{'form':form})
