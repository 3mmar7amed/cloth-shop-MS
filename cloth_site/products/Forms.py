from django import forms
from django.forms import fields
from products.models import products


class insertProductForm(forms.ModelForm):
    class Meta :
        model = products
        fields = [
            'product_id',
            'name',
            'sell_price',
            'buy_price',
            'num_of_items' ,
            'factory_name'
        ]

class sellForm(forms.Form):
    pay = forms.DecimalField(max_digits=19, decimal_places=10  )
    product_id = forms.CharField( max_length=100)

