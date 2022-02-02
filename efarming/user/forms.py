from django import forms

class vender_form(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    Email = forms.EmailField(max_length=200)
    phone_no = forms.NumberInput()
    address = forms.CharField()
    area_code = forms.IntegerField()
