from django import forms
from .models import Stock

class StockModelForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'price']
