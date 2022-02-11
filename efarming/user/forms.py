from django import forms
from .models import Vendor , user ,Customer

   

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor 

        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
