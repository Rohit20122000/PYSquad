
from django import forms
from .models import warehouse,ProductType,Catagory


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = warehouse
        fields = "__all__"


class ProductTypefForm(forms.ModelForm):
    class Meta:
        model =  ProductType
        fields = "__all__"


class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = "__all__"