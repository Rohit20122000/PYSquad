from pyexpat import model
from django import forms
from .models import Vendor , user
   

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor 

        fields = "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"
