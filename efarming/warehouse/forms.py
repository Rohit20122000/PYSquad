from django import forms
from .models import Warehouse,ProductType,Catagory,VendorInventory


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"


class ProductTypefForm(forms.ModelForm):
    class Meta:
        model =  ProductType
        fields = "__all__"


class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = "__all__"

class InventoryForm(forms.ModelForm):
    class Meta:
        model = VendorInventory
        fields = "__all__"
        exclude = 'is_accept',