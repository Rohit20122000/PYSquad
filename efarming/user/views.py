from django.shortcuts import render
from .forms import   VendorForm, UserForm , CustomerForm
# Create your views here.
    
def vendor_view(request):
 
    form = VendorForm(request.POST)
   
    if form.is_valid():
        form.save()
                 
    return render(request, "venderform.html",{'form':form})

def user_view(request):

    form = UserForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "userform.html",{'form':form})

def customer_view(request):

    form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "customerform.html",{'form':form})