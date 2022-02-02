from django.http import HttpResponse
from django.shortcuts import render
from .forms import vender_form

# Create your views here.
def vender_view(request):
    form = vender_form()
    return render(request, "venderform.html",{'form':form})
