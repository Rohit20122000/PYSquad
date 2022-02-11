from urllib import request
from django.shortcuts import render
from .forms import  VendorForm, UserForm
# Create your views here.
    
def vendor_view(request):
 
    form = VendorForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    

    #form = VendorForm()
    return render(request, "venderform.html",{'form':form})

def user_view(request):

    form = UserForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "venderform.html",{'form':form})

    